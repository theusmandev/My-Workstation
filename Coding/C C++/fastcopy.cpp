// fastcopy_win.cpp
// Windows advanced fast copy using FILE_FLAG_NO_BUFFERING, OVERLAPPED I/O, and IOCP
// Compile with (Developer Command Prompt):
// cl /std:c++17 /O2 /MD /DUNICODE /D_UNICODE fastcopy_win.cpp

#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <iostream>
#include <string>
#include <vector>
#include <atomic>
#include <stdexcept>
#include <cassert>
#include <iomanip>
#include <chrono>

struct HandleGuard {
    HANDLE h;
    HandleGuard(HANDLE h) : h(h) {}
    ~HandleGuard() { if (h != INVALID_HANDLE_VALUE) CloseHandle(h); }
};

struct Buffer {
    OVERLAPPED ov;
    char* data;            // page-aligned buffer (VirtualAlloc)
    DWORD bufSize;         // requested size (multiple of sector)
    ULONG64 fileOffset;    // offset for read/write
    DWORD validBytes;      // bytes actually read (for last chunk)
    enum State { IDLE=0, READ_PENDING=1, WRITE_PENDING=2 } state;
};

static std::atomic<bool> g_cancelled(false);

static BOOL WINAPI CtrlHandler(DWORD dwCtrlType) {
    if (dwCtrlType == CTRL_C_EVENT) {
        g_cancelled.store(true);
        return TRUE;
    }
    return FALSE;
}

static void die_last_error(const wchar_t* msg) {
    DWORD e = GetLastError();
    LPWSTR buf = nullptr;
    FormatMessageW(FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,
                   NULL, e, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT), (LPWSTR)&buf, 0, NULL);
    std::wcerr << msg << L": " << (buf ? buf : L"(unknown)") << L" (err=" << e << L")\n";
    if (buf) LocalFree(buf);
    exit(1);
}

static DWORD get_sector_size(const std::wstring& path) {
    wchar_t rootPath[MAX_PATH];
    if (!GetFullPathNameW(path.c_str(), MAX_PATH, rootPath, NULL)) die_last_error(L"GetFullPathNameW failed");
    rootPath[3] = L'\0'; // e.g., "C:\"
    DWORD sectorsPerCluster, bytesPerSector, numberOfFreeClusters, totalNumberOfClusters;
    if (!GetDiskFreeSpaceW(rootPath, &sectorsPerCluster, &bytesPerSector, &numberOfFreeClusters, &totalNumberOfClusters))
        die_last_error(L"GetDiskFreeSpaceW failed");
    return bytesPerSector;
}

int wmain(int argc, wchar_t** argv) {
    // Set Ctrl+C handler
    if (!SetConsoleCtrlHandler(CtrlHandler, TRUE)) die_last_error(L"SetConsoleCtrlHandler failed");

    if (argc < 3) {
        std::wcout << L"Usage: fastcopy_win <source> <destination> [buffer_mb=8] [concurrency=4]\n";
        return 1;
    }
    std::wstring src = argv[1];
    std::wstring dst = argv[2];
    size_t bufferMB = 8;
    int concurrency = 4;
    if (argc >= 4) bufferMB = std::max<size_t>(1, std::wcstoul(argv[3], nullptr, 10));
    if (argc >= 5) concurrency = std::max(1, std::stoi(argv[4]));

    // Query file size
    WIN32_FILE_ATTRIBUTE_DATA fad;
    if (!GetFileAttributesExW(src.c_str(), GetFileExInfoStandard, &fad)) die_last_error(L"GetFileAttributesExW failed for source");
    LARGE_INTEGER totalSize;
    totalSize.HighPart = fad.ftFileSizeHigh;
    totalSize.LowPart = fad.ftFileSizeLow;

    if (totalSize.QuadPart == 0) {
        std::wcerr << L"Source file size is zero.\n";
        return 1;
    }

    // Decide whether to use unbuffered I/O (disable for small files < 1MB)
    bool useUnbuffered = totalSize.QuadPart >= 1024 * 1024;
    DWORD fileFlags = useUnbuffered ? (FILE_FLAG_NO_BUFFERING | FILE_FLAG_OVERLAPPED | FILE_FLAG_SEQUENTIAL_SCAN) : FILE_FLAG_OVERLAPPED;

    DWORD sectorSize = useUnbuffered ? get_sector_size(src) : 4096; // default 4KB alignment if buffered
    std::wcout << L"Disk sector size: " << sectorSize << L" bytes\n";

    // Ensure buffer size is multiple of sectorSize
    DWORD bufSize = (DWORD)(bufferMB * 1024 * 1024);
    if (useUnbuffered && bufSize % sectorSize != 0) {
        bufSize = (bufSize / sectorSize) * sectorSize;
        if (bufSize == 0) bufSize = sectorSize;
        std::wcout << L"Adjusted buffer size to multiple of sector size: " << bufSize << L" bytes\n";
    }

    // Limit total buffer size to 1GB
    if ((ULONGLONG)bufSize * concurrency > 1024ULL * 1024 * 1024) {
        std::wcerr << L"Error: Total buffer size exceeds 1GB limit\n";
        return 1;
    }

    // Open source file
    HandleGuard hSrc(CreateFileW(src.c_str(),
                                 GENERIC_READ,
                                 FILE_SHARE_READ,
                                 NULL,
                                 OPEN_EXISTING,
                                 fileFlags,
                                 NULL));
    if (hSrc.h == INVALID_HANDLE_VALUE) die_last_error(L"CreateFileW(source) failed");

    // Create destination file
    HandleGuard hDst(CreateFileW(dst.c_str(),
                                 GENERIC_WRITE,
                                 0,
                                 NULL,
                                 CREATE_ALWAYS,
                                 fileFlags | FILE_ATTRIBUTE_NORMAL,
                                 NULL));
    if (hDst.h == INVALID_HANDLE_VALUE) die_last_error(L"CreateFileW(destination) failed");

    // Create IOCP and associate both handles
    HandleGuard iocp(CreateIoCompletionPort(INVALID_HANDLE_VALUE, NULL, 0, 0));
    if (!iocp.h) die_last_error(L"CreateIoCompletionPort failed");
    if (!CreateIoCompletionPort(hSrc.h, iocp.h, (ULONG_PTR)1, 0)) die_last_error(L"Associate src with IOCP failed");
    if (!CreateIoCompletionPort(hDst.h, iocp.h, (ULONG_PTR)2, 0)) die_last_error(L"Associate dst with IOCP failed");

    // Prepare buffers
    std::vector<Buffer> bufs(concurrency);
    for (int i = 0; i < concurrency; ++i) {
        ZeroMemory(&bufs[i].ov, sizeof(OVERLAPPED));
        bufs[i].bufSize = bufSize;
        bufs[i].data = (char*)VirtualAlloc(NULL, bufs[i].bufSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
        if (!bufs[i].data) die_last_error(L"VirtualAlloc failed");
        bufs[i].fileOffset = 0;
        bufs[i].validBytes = 0;
        bufs[i].state = Buffer::IDLE;
    }

    std::atomic<ULONG64> nextReadOffset(0);
    std::atomic<int> outstandingOperations(0);
    std::atomic<ULONG64> bytesCopied(0);
    auto startTime = std::chrono::high_resolution_clock::now();

    // Kick off initial reads
    auto post_read = [&](Buffer& b) -> bool {
        if (g_cancelled.load()) return false;
        ULONG64 off = nextReadOffset.fetch_add(b.bufSize);
        if (off >= (ULONG64)totalSize.QuadPart) {
            return false;
        }
        DWORD toRead = b.bufSize;
        if (off + toRead > (ULONG64)totalSize.QuadPart) {
            ULONG64 remaining = (ULONG64)totalSize.QuadPart - off;
            if (useUnbuffered) {
                DWORD sectors = (DWORD)((remaining + sectorSize - 1) / sectorSize);
                toRead = sectors * sectorSize;
                if (toRead > b.bufSize) toRead = b.bufSize;
            } else {
                toRead = (DWORD)remaining;
            }
        }

        ZeroMemory(&b.ov, sizeof(OVERLAPPED));
        b.ov.Offset = (DWORD)(off & 0xFFFFFFFF);
        b.ov.OffsetHigh = (DWORD)((off >> 32) & 0xFFFFFFFF);
        b.fileOffset = off;
        b.validBytes = 0;
        b.state = Buffer::READ_PENDING;
        DWORD bytesRead = 0;
        BOOL ok = ReadFile(hSrc.h, b.data, toRead, &bytesRead, &b.ov);
        if (!ok && GetLastError() != ERROR_IO_PENDING) {
            die_last_error(L"ReadFile failed");
        }
        outstandingOperations.fetch_add(1);
        return true;
    };

    for (int i = 0; i < concurrency; ++i) {
        if (!post_read(bufs[i])) break;
    }

    // Main completion loop
    bool done = false;
    const DWORD timeout_ms = 30000; // 30s timeout
    while (!done) {
        if (g_cancelled.load()) {
            std::wcout << L"\nCopy cancelled by user.\n";
            break;
        }

        DWORD bytesTransferred;
        ULONG_PTR completionKey;
        LPOVERLAPPED pOv;
        BOOL res = GetQueuedCompletionStatus(iocp.h, &bytesTransferred, &completionKey, &pOv, timeout_ms);
        if (!res && pOv == NULL && GetLastError() == WAIT_TIMEOUT) {
            std::wcerr << L"Warning: I/O operation timed out after " << timeout_ms << L"ms\n";
            continue;
        }
        if (!res) die_last_error(L"GetQueuedCompletionStatus failed");

        Buffer* b = (Buffer*)pOv;
        if (b->state == Buffer::READ_PENDING) {
            DWORD bytesRead = bytesTransferred;
            b->validBytes = bytesRead;
            outstandingOperations.fetch_sub(1);

            if (bytesRead == 0) {
                b->state = Buffer::IDLE;
            } else {
                ZeroMemory(&b->ov, sizeof(OVERLAPPED));
                b->ov.Offset = (DWORD)(b->fileOffset & 0xFFFFFFFF);
                b->ov.OffsetHigh = (DWORD)((b->fileOffset >> 32) & 0xFFFFFFFF);
                b->state = Buffer::WRITE_PENDING;
                DWORD bytesWritten = 0;
                BOOL ok = WriteFile(hDst.h, b.data, b->validBytes, &bytesWritten, &b->ov);
                if (!ok && GetLastError() != ERROR_IO_PENDING) {
                    die_last_error(L"WriteFile failed");
                }
                outstandingOperations.fetch_add(1);
            }

            if (!post_read(*b)) {
                // no more reads
            }
        } else if (b->state == Buffer::WRITE_PENDING) {
            DWORD bytesWritten = bytesTransferred;
            outstandingOperations.fetch_sub(1);
            bytesCopied.fetch_add(bytesWritten);
            b->state = Buffer::IDLE;

            if (!post_read(*b)) {
                // no more reads
            }
        } else {
            std::wcerr << L"Error: Unexpected buffer state " << b->state << L"\n";
            return 1;
        }

        // Check completion
        if (outstandingOperations.load() == 0 && nextReadOffset.load() >= (ULONG64)totalSize.QuadPart) {
            done = true;
        }

        // Progress display (update every 100MB)
        static DWORD lastShown = 0;
        DWORD copiedNow = (DWORD)(bytesCopied.load() / (1024 * 1024));
        if (copiedNow / 100 != lastShown / 100) {
            lastShown = copiedNow;
            double pct = (100.0 * bytesCopied.load()) / (double)totalSize.QuadPart;
            int barWidth = 20;
            int filled = (int)(pct * barWidth / 100.0);
            std::wcout << L"\r[";
            for (int i = 0; i < barWidth; ++i) std::wcout << (i < filled ? L"█" : L" ");
            std::wcout << L"] " << std::fixed << std::setprecision(2) << pct << L"% (" << copiedNow << L" MB)";
            std::wcout.flush();
        }
    }

    // Flush and report
    if (!g_cancelled.load() && !FlushFileBuffers(hDst.h)) die_last_error(L"FlushFileBuffers failed");

    auto endTime = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();
    double mbps = duration > 0 ? (bytesCopied.load() / (1024.0 * 1024.0)) / (duration / 1000.0) : 0;

    std::wcout << L"\nCopy " << (g_cancelled.load() ? L"cancelled" : L"complete") << L". Total bytes: " << bytesCopied.load();
    if (!g_cancelled.load()) std::wcout << L", Speed: " << std::fixed << std::setprecision(2) << mbps << L" MB/s";
    std::wcout << L"\n";

    // Cleanup buffers
    for (auto &b : bufs) {
        if (b.data) VirtualFree(b.data, 0, MEM_RELEASE);
    }

    return 0;
}