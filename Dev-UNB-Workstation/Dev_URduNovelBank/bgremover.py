# import os
# from rembg import remove
# from PIL import Image

# def remove_bg_from_folder(input_folder, output_folder):
#     # Agar output folder nahi hai to bana lo
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Sare files par loop chalao
#     for filename in os.listdir(input_folder):
#         if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
#             input_path = os.path.join(input_folder, filename)
#             output_path = os.path.join(output_folder, filename.replace(".jpg", ".png").replace(".jpeg", ".png"))

#             # Image open karo
#             with Image.open(input_path) as img:
#                 # Background remove
#                 output = remove(img)

#                 # Transparent PNG me save karo
#                 output.save(output_path, "PNG")

#             print(f"✅ Background removed: {filename}")

#     print("\n🎉 Saari images process ho gayi! Output folder:", output_folder)


# # Example run
# input_folder = r"D:\bano qudsiya novels"  # Jahan aapki original pics hain
# output_folder = r"D:\bano qudsiya novelsokok"# Jahan nayi pics save hongi

# remove_bg_from_folder(input_folder, output_folder)





#good with heay ml model

# import os
# from rembg import remove
# from PIL import Image
# import traceback
# from tqdm import tqdm

# def remove_bg_from_folder(input_folder, output_folder):
#     # Validate input folder
#     if not os.path.exists(input_folder):
#         print(f"❌ Error: Input folder '{input_folder}' does not exist!")
#         return

#     # Create output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Supported image extensions
#     supported_extensions = (".png", ".jpg", ".jpeg", ".webp")

#     # Get list of image files
#     image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_extensions)]
    
#     if not image_files:
#         print(f"⚠️ No images found in '{input_folder}'!")
#         return

#     # Process images with progress bar
#     for filename in tqdm(image_files, desc="Processing images"):
#         try:
#             input_path = os.path.join(input_folder, filename)
#             # Generate output filename (replace any extension with .png)
#             output_filename = os.path.splitext(filename)[0] + ".png"
#             output_path = os.path.join(output_folder, output_filename)

#             # Skip if output file already exists
#             if os.path.exists(output_path):
#                 print(f"⚠️ Skipped: '{output_filename}' already exists in output folder")
#                 continue

#             # Open and process image
#             with Image.open(input_path) as img:
#                 # Ensure image is in RGB mode (required by rembg)
#                 if img.mode != "RGB":
#                     img = img.convert("RGB")
#                 # Remove background
#                 output = remove(img)
#                 # Save as PNG
#                 output.save(output_path, "PNG")

#             print(f"✅ Background removed: {filename} -> {output_filename}")

#         except Exception as e:
#             print(f"❌ Error processing '{filename}': {str(e)}")
#             traceback.print_exc()

#     print("\n🎉 All images processed! Output folder:", output_folder)

# # Example run
# if __name__ == "__main__":
#     input_folder = r"D:\bano qudsiya novels"  # Replace with your input folder
#     output_folder = r"D:\bano qudsiya novelsokok"  # Replace with your output folder

#     remove_bg_from_folder(input_folder, output_folder)



# import os
# from rembg import remove
# from PIL import Image
# import traceback
# from tqdm import tqdm

# def remove_bg_from_folder(input_folder, output_folder):
#     if not os.path.exists(input_folder):
#         print(f"❌ Error: Input folder '{input_folder}' does not exist!")
#         return

#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     supported_extensions = (".png", ".jpg", ".jpeg", ".webp")
#     image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_extensions)]
    
#     if not image_files:
#         print(f"⚠️ No images found in '{input_folder}'!")
#         return

#     for filename in tqdm(image_files, desc="Processing images"):
#         try:
#             input_path = os.path.join(input_folder, filename)
#             output_filename = os.path.splitext(filename)[0] + ".png"
#             output_path = os.path.join(output_folder, output_filename)

#             if os.path.exists(output_path):
#                 print(f"⚠️ Skipped: '{output_filename}' already exists")
#                 continue

#             with Image.open(input_path) as img:
#                 if img.mode != "RGB":
#                     img = img.convert("RGB")
#                 # Use default model (u2net)
#                 output = remove(img)
#                 output.save(output_path, "PNG")

#             print(f"✅ Background removed: {filename} -> {output_filename}")

#         except Exception as e:
#             print(f"❌ Error processing '{filename}': {str(e)}")

#     print("\n🎉 All images processed! Output folder:", output_folder)

# if __name__ == "__main__":
#     input_folder = r"D:\bano qudsiya novels"
#     output_folder = r"D:\bano qudsiya novelsokok"
#     remove_bg_from_folder(input_folder, output_folder)








# import os
# import cv2
# import numpy as np
# from tqdm import tqdm

# def remove_white_bg(input_folder, output_folder):
#     # Check if input folder exists
#     if not os.path.exists(input_folder):
#         print(f"❌ Input folder '{input_folder}' not found!")
#         return

#     # Create output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Supported image extensions
#     supported_extensions = (".png", ".jpg", ".jpeg", ".webp")
#     image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_extensions)]
    
#     if not image_files:
#         print(f"⚠️ No images found in '{input_folder}'!")
#         return

#     # Process images with progress bar
#     for filename in tqdm(image_files, desc="Processing images"):
#         try:
#             input_path = os.path.join(input_folder, filename)
#             output_filename = os.path.splitext(filename)[0] + ".png"
#             output_path = os.path.join(output_folder, output_filename)

#             # Skip if output file already exists
#             if os.path.exists(output_path):
#                 print(f"⚠️ Skipped: '{output_filename}' already exists")
#                 continue

#             # Read image
#             img = cv2.imread(input_path)
#             if img is None:
#                 print(f"❌ Failed to load '{filename}'")
#                 continue

#             # Convert to grayscale
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             # Threshold to isolate white background (adjust 240 if needed)
#             _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
#             # Create transparent image
#             img_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#             img_rgba[:, :, 3] = mask  # Set alpha channel
#             # Save as PNG
#             cv2.imwrite(output_path, img_rgba)
#             print(f"✅ Processed: {filename} -> {output_filename}")

#         except Exception as e:
#             print(f"❌ Error processing '{filename}': {str(e)}")

#     print("\n🎉 All images processed! Output folder:", output_folder)

# if __name__ == "__main__":
#     input_folder = r"D:\bano qudsiya novels"
#     output_folder = r"D:\bano qudsiya novelsokok"
#     remove_white_bg(input_folder, output_folder)






import os
from PIL import Image

def remove_white_bg(input_folder, output_folder, threshold=240):
    os.makedirs(output_folder, exist_ok=True)

    files = os.listdir(input_folder)
    if not files:
        print("⚠️ Input folder khali hai!")
        return

    for filename in files:
        input_path = os.path.join(input_folder, filename)

        if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".webp")):
            print(f"⏩ Skip: {filename} (image nahi hai)")
            continue

        try:
            output_name = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, output_name)

            img = Image.open(input_path).convert("RGBA")
            datas = img.getdata()

            new_data = []
            for item in datas:
                if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)

            img.putdata(new_data)
            img.save(output_path, "PNG")
            print(f"✅ Done: {output_name}")

        except Exception as e:
            print(f"❌ Error {filename}: {e}")

    print("\n🎉 Processing complete! Dekho output folder:", output_folder)


# Yahan apna folder ka full path do (r"" use karo taake \ problem na de)
input_folder = r"D:\bano qudsiya novels"
output_folder = r"D:\bano qudsiya novels\output"

remove_white_bg(input_folder, output_folder)
