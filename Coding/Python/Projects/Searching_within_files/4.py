'''
Progress bar updates in real-time as each file is processed.

Shows how many files are scanned and how many are left.

Works perfectly with multi-threading for speed and efficiency
'''

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from docx import Document
from PyPDF2 import PdfReader
from tqdm import tqdm  # For progress bar

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
                return None  # Skip corrupted DOCX

        # Handle PDF files
        elif file_path.lower().endswith(".pdf"):
            try:
                pdf = PdfReader(file_path)
                for page in pdf.pages:
                    content += page.extract_text() or ""
            except Exception:
                return None  # Skip corrupted PDF
        else:
            return None  # Skip unsupported file types

        # Search phrase (case-insensitive)
        if phrase.lower() in content.lower():
            return file_path
        else:
            return None
    
    except Exception:
        return None  # Skip any other error


# ------------------------
# Multi-threaded search with progress bar
# ------------------------
def search_phrase_in_files_multithread(folder_path, phrase, max_threads=8):
    all_files = []
    
    # Collect all candidate files first
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".txt", ".docx", ".pdf")):
                all_files.append(os.path.join(root, file))
    
    found_files = []

    # Show progress bar
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(search_in_file, file, phrase): file for file in all_files}
        
        for future in tqdm(as_completed(futures), total=len(futures), desc="Searching Files", unit="file"):
            result = future.result()
            if result:
                found_files.append(result)
    
    return found_files


# ------------------------
# Example Usage
# ------------------------
if __name__ == "__main__":
    folder = r"C:\Users\PCS\Downloads\unb"  # Change to your folder path
    phrase = "Usman"
    
    results = search_phrase_in_files_multithread(folder, phrase, max_threads=8)
    
    if results:
        print("\nFound in:")
        for file in results:
            print(file)
    else:
        print("\nNo files found with that phrase.")
