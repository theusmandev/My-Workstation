
''''
GUI built with Tkinter

Browse button to select folder

Search phrase input

Real-time progress bar

Scrollable list to view results
scroll
Multi-threaded search for speed

Responsive GUI (search runs in a background thread)


'''
import os
import threading
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from concurrent.futures import ThreadPoolExecutor, as_completed
from docx import Document
from PyPDF2 import PdfReader

SUPPORTED_EXTENSIONS = (".txt", ".docx", ".pdf")

# ------------------------
# Function to search inside a single file
# ------------------------
def search_in_file(file_path, phrase):
    content = ""
    ext = file_path.lower()

    try:
        # TXT files
        if ext.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

        # DOCX files
        elif ext.endswith(".docx"):
            try:
                doc = Document(file_path)
                content = "\n".join([para.text for para in doc.paragraphs])
            except Exception:
                return None

        # PDF files
        elif ext.endswith(".pdf"):
            try:
                pdf = PdfReader(file_path)
                for page in pdf.pages:
                    content += page.extract_text() or ""
            except Exception:
                return None

        else:
            return None  # Skip unsupported

        # Search phrase (case-insensitive)
        if phrase.lower() in content.lower():
            return file_path
        else:
            return None

    except Exception:
        return None  # Skip errors


# ------------------------
# GUI App
# ------------------------
class FileSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Search Tool")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        # Variables
        self.folder_path = StringVar()
        self.search_phrase = StringVar()

        # Folder selection
        Label(root, text="Folder:").pack(anchor=W, padx=10, pady=5)
        folder_frame = Frame(root)
        folder_frame.pack(fill=X, padx=10)
        Entry(folder_frame, textvariable=self.folder_path, width=50).pack(side=LEFT, fill=X, expand=True)
        Button(folder_frame, text="Browse", command=self.browse_folder).pack(side=LEFT, padx=5)

        # Search phrase input
        Label(root, text="Search Phrase:").pack(anchor=W, padx=10, pady=5)
        Entry(root, textvariable=self.search_phrase, width=50).pack(fill=X, padx=10)

        # Progress bar
        self.progress = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)

        # Results list
        self.result_list = Listbox(root, height=15)
        self.result_list.pack(fill=BOTH, expand=True, padx=10, pady=5)
        scrollbar = Scrollbar(self.result_list, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.result_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_list.yview)

        # Search button
        Button(root, text="Search", command=self.start_search).pack(pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def start_search(self):
        folder = self.folder_path.get()
        phrase = self.search_phrase.get()

        if not folder or not phrase:
            messagebox.showwarning("Warning", "Please select a folder and enter a search phrase.")
            return

        # Clear old results
        self.result_list.delete(0, END)
        self.progress['value'] = 0

        # Run search in a separate thread (so GUI stays responsive)
        threading.Thread(target=self.search_files, args=(folder, phrase), daemon=True).start()

    def search_files(self, folder, phrase):
        all_files = [
            os.path.join(root, file)
            for root, dirs, files in os.walk(folder)
            for file in files
            if file.lower().endswith(SUPPORTED_EXTENSIONS)
        ]

        if not all_files:
            messagebox.showinfo("Info", "No supported files found in the selected folder.")
            return

        total_files = len(all_files)
        found_files = []

        # Multi-threaded search
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(search_in_file, file, phrase): file for file in all_files}

            for idx, future in enumerate(as_completed(futures), 1):
                result = future.result()
                if result:
                    found_files.append(result)
                    self.result_list.insert(END, result)

                # Update progress bar
                self.progress['value'] = (idx / total_files) * 100

        if not found_files:
            messagebox.showinfo("Result", "No files found with that phrase.")
        else:
            messagebox.showinfo("Result", f"Search completed. Found in {len(found_files)} file(s).")


# ------------------------
# Run GUI App
# ------------------------
if __name__ == "__main__":
    root = Tk()
    app = FileSearchApp(root)
    root.mainloop()
