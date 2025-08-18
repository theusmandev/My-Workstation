#only for txt files

import os

def search_phrase_in_files(folder_path, phrase):
    found_files = []
    
    # Walk through the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):  # First, we check only text files
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        if phrase.lower() in content.lower():  # Case-insensitive search
                            found_files.append(file_path)
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")
    
    return found_files


# Example usage
folder = r"C:\Users\PCS\Downloads" # Change to your folder path
phrase = "nayapay"
results = search_phrase_in_files(folder, phrase)

if results:
    print("Found in:")
    for file in results:
        print(file)
else:
    print("No files found with that phrase.")
