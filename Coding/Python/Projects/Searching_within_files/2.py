'''
Corrupted PDF and DOCX files are skipped automatically

errors="ignore" used for text files → no crash on weird characters

Prints a friendly message when a file is skipped instead of stopping


'''


import os
from docx import Document
from PyPDF2 import PdfReader

def search_phrase_in_files(folder_path, phrase):
    found_files = []
    
    # Walk through all files in the folder and subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # We will store content here (empty by default)
            content = ""
            
            try:
                # Handle TXT files
                if file.lower().endswith(".txt"):
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                
                # Handle DOCX files
                elif file.lower().endswith(".docx"):
                    try:
                        doc = Document(file_path)
                        content = "\n".join([para.text for para in doc.paragraphs])
                    except Exception:
                        print(f"[Skipped Corrupted DOCX] {file_path}")
                        continue
                
                # Handle PDF files
                elif file.lower().endswith(".pdf"):
                    try:
                        pdf = PdfReader(file_path)
                        for page in pdf.pages:
                            content += page.extract_text() or ""
                    except Exception:
                        print(f"[Skipped Corrupted PDF] {file_path}")
                        continue
                
                else:
                    continue  # Skip unsupported file types
                
                # Search for the phrase (case-insensitive)
                if phrase.lower() in content.lower():
                    found_files.append(file_path)
            
            except Exception as e:
                print(f"[Skipped Error] {file_path}: {e}")
    
    return found_files


# ------------------------
# Example Usage
# ------------------------
if __name__ == "__main__":
    folder = r"C:\Users\PCS\Downloads\unb"  # Change to your folder path
    phrase = "CS"
    
    results = search_phrase_in_files(folder, phrase)
    
    if results:
        print("\nFound in:")
        for file in results:
            print(file)
    else:
        print("\nNo files found with that phrase.")
