from PIL import Image
import os

def images_to_pdf(folder_path, output_pdf):
    # Folder ke andar jitni bhi images hain, unke paths le lo
    images = []
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, file_name)
            images.append(img_path)

    if not images:
        print("No images found in the folder!")
        return

    # Pehli image ko open karo (as base)
    first_image = Image.open(images[0]).convert("RGB")

    # Baaki sab ko convert karke list me dalo
    rest_images = [Image.open(img).convert("RGB") for img in images[1:]]

    # Sab ko ek PDF me save karo
    first_image.save(output_pdf, save_all=True, append_images=rest_images)
    print(f"✅ PDF created successfully: {output_pdf}")

# Example use:
folder_path = r"E:\Quotive\1" # ← apna folder path likho
output_pdf = r"E:\Quotive\1.pdf"  # ← output file ka naam
images_to_pdf(folder_path, output_pdf)
