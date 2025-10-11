#!/usr/bin/env python3
"""
Laptop Audit Script
-------------------
Usage:
- Copy this file to a USB stick or keep it on your phone/cloud.
- At the shop, run it on the target laptop (requires Python 3).
  Windows: double-click or run `python laptop_audit.py` in Command Prompt / PowerShell
  Linux/macOS: `python3 laptop_audit.py`

What it collects (best-effort):
- OS, architecture, platform info
- CPU model, cores, logical processors, frequency
- Total RAM size
- Disk models and sizes
- GPU/Video controllers
- BIOS / Serial number (if available)
- Motherboard / Model / Manufacturer (if available)
- Battery status (if available)
- Network adapters & MAC addresses
- Installed Python (if any)
- A summary score & checklist you can use when buying a laptop

Output:
- Prints to console
- Saves a detailed report as 'laptop_report.txt' in the same folder
"""

import platform
import subprocess
import sys
import os
import datetime
from pathlib import Path

# Output report path (same folder)
REPORT_PATH = Path.cwd() / "laptop_report.txt"

def run(cmd, shell=False, text=True):
    try:
        result = subprocess.check_output(cmd, shell=shell, stderr=subprocess.STDOUT, text=text)
        return result.strip()
    except Exception as e:
        return f"[error running `{cmd}`: {e}]"

def header(title):
    return f"\n{'='*8} {title} {'='*8}\n"

def gather_windows():
    out = []
    out.append(header("Windows System Info"))
    out.append(run(["wmic", "OS", "get", "Caption,Version,OSArchitecture", "/format:list"]))
    out.append(header("CPU"))
    out.append(run(["wmic", "cpu", "get", "Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed", "/format:list"]))
    out.append(header("BIOS / Serial"))
    out.append(run(["wmic", "bios", "get", "Manufacturer,SMBIOSBIOSVersion,SerialNumber,ReleaseDate", "/format:list"]))
    out.append(header("System / Baseboard"))
    out.append(run(["wmic", "computersystem", "get", "Manufacturer,Model", "/format:list"]))
    out.append(run(["wmic", "baseboard", "get", "Manufacturer,Product,SerialNumber", "/format:list"]))
    out.append(header("Memory (RAM)"))
    mem = run(["wmic", "MemoryChip", "get", "Capacity,Manufacturer,Speed,DeviceLocator", "/format:list"])
    if "error" in mem.lower():
        out.append(run(["systeminfo"]))
    else:
        out.append(mem)
    out.append(header("Disk Drives"))
    out.append(run(["wmic", "diskdrive", "get", "Model,Size,InterfaceType", "/format:list"]))
    out.append(header("Video Controllers (GPU)"))
    out.append(run(["wmic", "path", "win32_VideoController", "get", "Name,DriverVersion,AdapterRAM", "/format:list"]))
    out.append(header("Battery (if present)"))
    out.append(run(["wmic", "path", "Win32_Battery", "get", "EstimatedChargeRemaining,BatteryStatus,Name", "/format:list"]))
    out.append(header("Network / MAC Addresses"))
    out.append(run(["getmac", "/v", "/fo", "list"]))
    out.append(header("Python"))
    out.append(run([sys.executable, "--version"]))
    dx = run(["powershell", "-Command", "Get-CimInstance -ClassName Win32_PnPSignedDriver | where {$_.DeviceClass -eq 'Display'} | Select-Object DeviceName,DriverVersion"], shell=False)
    out.append(header("Display Drivers (powershell)"))
    out.append(dx)
    return "\n".join(out)

def gather_linux():
    out = []
    out.append(header("Linux System Info"))
    out.append(run(["lsb_release", "-a"]))
    out.append(run(["uname", "-a"]))
    out.append(header("CPU"))
    out.append(run(["lscpu"]))
    out.append(header("Memory"))
    out.append(run(["free", "-h"]))
    out.append(header("Disks (lsblk)"))
    out.append(run(["lsblk", "-o", "NAME,SIZE,MODEL"]))
    out.append(header("PCI Devices (GPU)"))
    out.append(run(["lspci", "-nnk | grep -i vga -A3"], shell=True))
    out.append(header("DMI / System (may need root)"))
    out.append(run(["sudo", "dmidecode", "-t", "system"], shell=False))
    out.append(header("Network Interfaces"))
    out.append(run(["ip", "addr"], shell=False))
    return "\n".join(out)

def gather_macos():
    out = []
    out.append(header("macOS System Info"))
    out.append(run(["sw_vers"]))
    out.append(header("Hardware Overview"))
    out.append(run(["system_profiler", "SPHardwareDataType"]))
    out.append(header("Memory"))
    out.append(run(["system_profiler", "SPMemoryDataType"]))
    out.append(header("GPUs"))
    out.append(run(["system_profiler", "SPDisplaysDataType"]))
    out.append(header("Storage"))
    out.append(run(["system_profiler", "SPStorageDataType"]))
    return "\n".join(out)

def quick_checks(report_text):
    import re
    checks = []
    checks.append("Quick Buying Checklist:")
    cores = re.search(r"NumberOfCores.*?(\d+)", report_text) or re.search(r"CPU\(s\):\s+(\d+)", report_text)
    threads = re.search(r"NumberOfLogicalProcessors.*?(\d+)", report_text) or re.search(r"Thread\(s\) per", report_text)
    if cores:
        checks.append(f"- Physical cores detected: {cores.group(1)}")
    if threads:
        checks.append(f"- Logical processors / threads detected: {threads.group(1)}")
    import math
    ram_mb = None
    m = re.search(r"Total Physical Memory:\s+([\d,]+)", report_text)
    if m:
        ram_mb = int(m.group(1).replace(",",""))//(1024*1024)
    else:
        m = re.search(r"Memory:\s+([0-9\.]+)(\s?G)", report_text)
        if m and m.group(2).strip().upper().startswith("G"):
            ram_mb = int(float(m.group(1))*1024)
    if ram_mb:
        checks.append(f"- Approx RAM: {ram_mb} MB")
    if "EstimatedChargeRemaining" in report_text or "Battery" in report_text:
        checks.append("- Battery info present.")
    if any(x in report_text for x in ["Video Controller", "VGA", "NVIDIA", "AMD", "Intel"]):
        checks.append("- GPU detected (check model in detailed report).")
    checks.append("- Save this report and compare with seller specs.")
    return "\n".join(checks)

def main():
    out_lines = []
    now = datetime.datetime.now().isoformat()
    out_lines.append(f"Generated: {now}")
    out_lines.append(f"Run on: {platform.platform()}")
    out_lines.append(header("SUMMARY"))
    system = platform.system()
    try:
        if system == "Windows":
            out_lines.append(gather_windows())
        elif system == "Linux":
            out_lines.append(gather_linux())
        elif system == "Darwin":
            out_lines.append(gather_macos())
        else:
            out_lines.append(f"Unsupported OS: {system}\nTrying generic commands...")
            out_lines.append(run(["uname", "-a"], shell=False))
    except Exception as e:
        out_lines.append(f"[Error gathering system info: {e}]")

    report_text = "\n".join(out_lines)
    summary = quick_checks(report_text)
    final = summary + "\n\n" + report_text

    try:
        REPORT_PATH.write_text(final, encoding="utf-8")
        print("\n" + "="*10 + " QUICK SUMMARY " + "="*10 + "\n")
        print(summary)
        print("\nDetailed report saved to:", REPORT_PATH)
    except Exception as e:
        print("Could not save report file:", e)
        print("\nFull report follows:\n")
        print(final)

if __name__ == "__main__":
    main()
