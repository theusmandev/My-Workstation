'''
Multi-threading → Uses 8 threads by default, you can increase if your CPU has more cores.

Parallel search → Several files are searched at the same time, making it much faster for large folders.

Robust error handling → Still skips corrupted or unreadable files without crashing.
'''

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from docx import Document
from PyPDF2 import PdfReader

# ------------------------
# Function to search inside a single file
# ------------------------
def search_in_file(file_path, phrase):
    content = ""
    try:
        # Handle TXT files
        if file_path.lower().endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

        # Handle DOCX files
        elif file_path.lower().endswith(".docx"):
            try:
                doc = Document(file_path)
                content = "\n".join([para.text for para in doc.paragraphs])
            except Exception:
                print(f"[Skipped Corrupted DOCX] {file_path}")
                return None

        # Handle PDF files
        elif file_path.lower().endswith(".pdf"):
            try:
                pdf = PdfReader(file_path)
                for page in pdf.pages:
                    content += page.extract_text() or ""
            except Exception:
                print(f"[Skipped Corrupted PDFs] {file_path}")
                return None
        else:
            return None  # Skip unsupported file types

        # Search phrase (case-insensitive)
        if phrase.lower() in content.lower():
            return file_path
        else:
            return None
    
    except Exception as e:
        print(f"[Skipped Errors] {file_path}: {e}")
        return None

# ------------------------
# Main function using multi-threading
# ------------------------
def search_phrase_in_files_multithread(folder_path, phrase, max_threads=8):
    all_files = []
    
    # Collect all candidate files first
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".txt", ".docx", ".pdf")):
                all_files.append(os.path.join(root, file))
    
    found_files = []
    
    # Use ThreadPoolExecutor to process files in parallel
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(search_in_file, file, phrase): file for file in all_files}
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                found_files.append(result)
    
    return found_files

# ------------------------
# Example Usage
# ------------------------
if __name__ == "__main__":
    folder = r"C:\Users\PCS\Downloads\unb"  # Change to your folder path
    phrase = "CS"
    
    results = search_phrase_in_files_multithread(folder, phrase, max_threads=8)
    
    if results:
        print("\nFound in:")
        for file in results:
            print(file)
    else:
        print("\nNo files found with that phrase.")
