import os

# Specify the folder path
folder_path = r"C:\Users\Latitude\Downloads\uns"  # Replace with your folder path
output_file = "file_names.txt"  # Name of the output TXT file

# Extract all file names
try:
    file_names = os.listdir(folder_path)
    
    # Save file names to a TXT file
    with open(output_file, "w", encoding="utf-8") as file:
        for name in file_names:
            file.write(name + "\n")
    
    print(f"All file names have been saved to '{output_file}'.")
except Exception as e:
    print(f"An error occurred: {e}")
