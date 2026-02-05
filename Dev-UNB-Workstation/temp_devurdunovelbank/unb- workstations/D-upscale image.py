import os
from PIL import Image, ImageEnhance, ImageFilter

def enhance_and_upscale_images(input_folder):
    output_folder = os.path.join(input_folder, "enhanced")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            file_path = os.path.join(input_folder, filename)
            img = Image.open(file_path)

            # 🧠 Step 1: Upscale (2x)
            new_size = (img.width * 2, img.height * 2)
            img = img.resize(new_size, Image.LANCZOS)

            # 🧠 Step 2: Slight noise reduction + sharpen
            img = img.filter(ImageFilter.SMOOTH_MORE)
            img = img.filter(ImageFilter.SHARPEN)

            # 🧠 Step 3: Enhance colors and contrast
            img = ImageEnhance.Color(img).enhance(1.4)      # +40% saturation
            img = ImageEnhance.Contrast(img).enhance(1.3)   # +30% contrast
            img = ImageEnhance.Brightness(img).enhance(1.1) # +10% brightness
            img = ImageEnhance.Sharpness(img).enhance(1.2)  # +20% sharpness

            # 🧠 Step 4: Save to output folder
            output_path = os.path.join(output_folder, filename)
            img.save(output_path, "PNG")

            print(f"✅ Enhanced: {filename}")

    print(f"\n🎉 All done! Enhanced images saved to: {output_folder}")

# 🧩 Hardcoded path (👉 change this to your folder)
if __name__ == "__main__":
    folder_path = r"E:\kiran complete\2006 - Copy\pngs" # <--- apna path yahan likho
    enhance_and_upscale_images(folder_path)
