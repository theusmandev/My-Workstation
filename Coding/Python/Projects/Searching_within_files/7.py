'''
Shows a snippet (context) around the first match of the phrase (default ±60 characters).

Snippet removes line breaks for cleaner display.



'''

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from docx import Document
from PyPDF2 import PdfReader
from tqdm import tqdm

SUPPORTED_EXTENSIONS = (".txt", ".docx", ".pdf")

# ------------------------
# Function to search inside a single file with snippet
# ------------------------
def search_in_file(file_path, phrase, snippet_length=60):
    content = ""
    ext = file_path.lower()

    try:
        # Handle TXT files
        if ext.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

        # Handle DOCX files
        elif ext.endswith(".docx"):
            try:
                doc = Document(file_path)
                content = "\n".join([para.text for para in doc.paragraphs])
            except Exception:
                return None

        # Handle PDF files
        elif ext.endswith(".pdf"):
            try:
                pdf = PdfReader(file_path)
                for page in pdf.pages:
                    content += page.extract_text() or ""
            except Exception:
                return None

        else:
            return None  # Skip unsupported files

        # Case-insensitive search
        lower_content = content.lower()
        lower_phrase = phrase.lower()

        if lower_phrase in lower_content:
            index = lower_content.index(lower_phrase)
            
            # Generate a snippet around the found phrase
            start = max(index - snippet_length, 0)
            end = min(index + len(phrase) + snippet_length, len(content))
            snippet = content[start:end].replace("\n", " ")
            
            return (file_path, snippet.strip())
        else:
            return None
    
    except Exception:
        return None


# ------------------------
# Multi-threaded search with snippets and progress bar
# ------------------------
def search_phrase_in_files_multithread(folder_path, phrase, max_threads=8):
    # Collect only supported files
    all_files = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(folder_path)
        for file in files
        if file.lower().endswith(SUPPORTED_EXTENSIONS)
    ]

    results = []

    # Use ThreadPoolExecutor with progress bar
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(search_in_file, file, phrase): file for file in all_files}
        
        for future in tqdm(as_completed(futures), total=len(futures), desc="Searching Files", unit="file"):
            result = future.result()
            if result:
                results.append(result)
    
    return results


# ------------------------
# Example Usage
# ------------------------
if __name__ == "__main__":
    folder = r""  # Change to your folder path
    phrase = "usman"
    
    results = search_phrase_in_files_multithread(folder, phrase, max_threads=8)
    
    if results:
        print("\nFound in:")
        for file, snippet in results:
            print(f"\nFile: {file}\nSnippet: ...{snippet}...")
    else:
        print("\nNo files found with that phrase.")
