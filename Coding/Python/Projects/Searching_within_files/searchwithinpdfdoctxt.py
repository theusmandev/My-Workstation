#search within pdfs,txts,docs,  version 1

import os
from docx import Document
from PyPDF2 import PdfReader

def search_phrase_in_files(folder_path, phrase):
    found_files = []
    
    # Walk through all files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Handle TXT files
                if file.lower().endswith(".txt"):
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                
                # Handle DOCX files
                elif file.lower().endswith(".docx"):
                    doc = Document(file_path)
                    content = "\n".join([para.text for para in doc.paragraphs])
                
                # Handle PDF files
                elif file.lower().endswith(".pdf"):
                    pdf = PdfReader(file_path)
                    content = ""
                    for page in pdf.pages:
                        content += page.extract_text() or ""
                
                else:
                    continue  # Skip other file types

                # Search phrase (case-insensitive)
                if phrase.lower() in content.lower():
                    found_files.append(file_path)
            
            except Exception as e:
                print(f"Could not read {file_path}: {e}")
    
    return found_files


# Example usage
folder = r""# Change to your folder path
phrase = "usman"
results = search_phrase_in_files(folder, phrase)

if results:
    print("\nFound in:")
    for file in results:
        print(file)
else:
    print("\nNo files found with that phrase.")
