import os
from rembg import remove
from PIL import Image

# Input aur Output folders
input_folder = r"C:\Users\Latitude\Downloads\images"   # apna folder path idhar dalen
output_folder = r"C:\Users\Latitude\Downloads\images_nobg"

# Agar output folder exist nahi karta to bana lo
os.makedirs(output_folder, exist_ok=True)

# Sab images par loop
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".png")

        with open(input_path, "rb") as inp_file:
            input_data = inp_file.read()
            output_data = remove(input_data)

        # Save background removed image
        with open(output_path, "wb") as out_file:
            out_file.write(output_data)

print("✅ Background remove ho gaya aur naya folder me save ho gaya.")
