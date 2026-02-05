import os
from PIL import Image
import pytesseract

# Pytesseract ka path set karein agar zarurat ho (Windows users ke liye):
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def rename_images_by_title(folder_path):
    """
    Folder mein har image ko OCR se process karein aur extracted title ko image ka naam banayen.
    """
    try:
        # Folder ke andar har file ko iterate karein
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Sirf images ko process karein
            if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff')):
                try:
                    # Image ko OCR ke zariye text me convert karein
                    image = Image.open(file_path)
                    extracted_text = pytesseract.image_to_string(image, lang='urd')

                    # Text ko saf karein (extra spaces aur line breaks hataein)
                    extracted_text = extracted_text.strip().replace("\n", " ")

                    # Agar text empty hai to skip karein
                    if not extracted_text:
                        print(f"No text found in {filename}, skipping...")
                        continue

                    # Valid filename ke liye characters ko sanitize karein
                    sanitized_text = "".join(c for c in extracted_text if c.isalnum() or c in " _-").strip()

                    # Naya filename banayen
                    new_filename = f"{sanitized_text}.jpg"
                    new_file_path = os.path.join(folder_path, new_filename)

                    # Rename karein agar naya naam unique ho
                    if not os.path.exists(new_file_path):
                        os.rename(file_path, new_file_path)
                        print(f"Renamed {filename} to {new_filename}")
                    else:
                        print(f"File with name {new_filename} already exists, skipping...")

                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    except Exception as e:
        print(f"Error accessing folder: {e}")

# User input folder path
folder_path = input("Enter the folder path containing novel cover images: ").strip()
rename_images_by_title(folder_path)
