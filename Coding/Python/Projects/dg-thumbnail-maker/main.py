
import cv2
import numpy as np
import os
import math
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

# --- 📁 فولڈرز اور سیٹنگز ---
input_folder = r"C:\Users\PCS\Downloads\New folder"
output_folder = os.path.join(input_folder, 'thumbnails_with_watermark')
os.makedirs(output_folder, exist_ok=True)

# پہلے پروگرام والا رنگ (رنگ بدلنے کے لیے)
content_hex_color = "#FFEFD5" 
# کینوس کا بیک گراؤنڈ رنگ (Beige)
canvas_bg_color = (245, 230, 205) 

# تھمب نیل سائز
thumb_width, thumb_height = 1200, 800
blur_radius = 25
shadow_opacity = 90
shadow_offset = (15, 15)

# 🖋️ واٹر مارک سیٹنگز
watermark_text = "www.urdunovelbanks.com"
font_path = r"E:\unb-workstation\Writers All Novels\RobotoCondensed-BoldItalic.ttf" # اپنا فونٹ پاتھ یہاں چیک کر لیں

try:
    font = ImageFont.truetype(font_path, 32)
except IOError:
    print("⚠️ Font nahi mila! Default use ho raha hai.")
    font = ImageFont.load_default()

# --- 🛠️ مددگار فنکشنز (Helper Functions) ---

def hex_to_bgr(hex_str):
    hex_str = hex_str.lstrip('#')
    rgb = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
    return np.array([rgb[2], rgb[1], rgb[0]], dtype=np.float32)

def get_best_text_color(bg_color):
    """بیک گراؤنڈ کے حساب سے کالا یا سفید رنگ منتخب کرتا ہے"""
    r, g, b = bg_color
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return (0, 0, 0, 255) if luminance > 0.5 else (255, 255, 255, 255)

def create_vertical_watermark(bg_color):
    """عمودی واٹر مارک (نیچے سے اوپر) بناتا ہے"""
    text_color = get_best_text_color(bg_color)
    
    # عارضی امیج ٹیکسٹ سائز معلوم کرنے کے لیے
    temp_img = Image.new("RGBA", (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    try:
        bbox = temp_draw.textbbox((0, 0), watermark_text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    except:
        tw, th = font.getsize(watermark_text)

    padding = 20
    txt_img = Image.new("RGBA", (tw + padding, th + padding), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt_img)
    d.text((padding//2, padding//2), watermark_text, font=font, fill=text_color)
    
    # 90 ڈگری روٹیٹ (Bottom to Top)
    return txt_img.rotate(90, expand=True)

# --- 🔁 مین پروسیسنگ لوپ ---

def main():
    target_color_bgr = hex_to_bgr(content_hex_color)
    counter = 1

    print("🚀 Processing started...")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            img_path = os.path.join(input_folder, filename)
            
            # 1. OpenCV: رنگ تبدیل کرنا
            cv_img = cv2.imread(img_path)
            if cv_img is None: continue
            
            img_float = cv_img.astype(np.float32) / 255.0
            colored_img = img_float * target_color_bgr
            colored_img = np.clip(colored_img, 0, 255).astype(np.uint8)
            
            # PIL میں کنورٹ کریں
            img_rgb = cv2.cvtColor(colored_img, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(img_rgb).convert("RGBA")

            # 2. PIL: تھمب نیل ڈیزائن
            # کنٹراسٹ بہتر کریں
            pil_img = ImageEnhance.Contrast(pil_img.convert("RGB")).enhance(1.1).convert("RGBA")
            
            # ری سائز
            max_h = int(thumb_height * 0.85)
            pil_img.thumbnail((thumb_width, max_h), Image.LANCZOS)

            # پوزیشن
            x = (thumb_width - pil_img.width) // 2
            y = (thumb_height - pil_img.height) // 2

            # شیڈو (Shadow)
            shadow_canvas = Image.new("RGBA", (pil_img.width + blur_radius*2, pil_img.height + blur_radius*2), (0,0,0,0))
            ImageDraw.Draw(shadow_canvas).rectangle(
                [blur_radius, blur_radius, pil_img.width + blur_radius, pil_img.height + blur_radius], 
                fill=(0, 0, 0, shadow_opacity)
            )
            shadow_canvas = shadow_canvas.filter(ImageFilter.GaussianBlur(blur_radius))

            # فائنل کینوس
            final_thumb = Image.new("RGB", (thumb_width, thumb_height), canvas_bg_color)
            final_thumb.paste(shadow_canvas, (x + shadow_offset[0] - blur_radius, y + shadow_offset[1] - blur_radius), shadow_canvas)
            final_thumb.paste(pil_img, (x, y), pil_img)

            # 3. واٹر مارک شامل کرنا
            watermark = create_vertical_watermark(canvas_bg_color)
            wm_x = x + pil_img.width + 50# تصویر کے دائیں طرف تھوڑا فاصلہ
            wm_y = y + (pil_img.height - watermark.height) // 2
            
            # اگر واٹر مارک کینوس سے باہر جا رہا ہو تو ایڈجسٹ کریں
            if wm_x + watermark.width > thumb_width:
                wm_x = thumb_width - watermark.width - 10

            final_thumb.paste(watermark, (wm_x, wm_y), watermark)

            # 4. سیو کرنا
            output_filename = f"www.urdunovelbanks.com({counter}).webp"
            final_thumb.save(os.path.join(output_folder, output_filename), "WEBP", quality=90)
            
            print(f"✅ Generated: {output_filename}")
            counter += 1

    print(f"\n✨ مبارک ہو! تمام {counter-1} تھمب نیلز واٹر مارک کے ساتھ تیار ہیں۔")

if __name__ == "__main__":
    main()












#v5
# import cv2
# import numpy as np
# import os
# from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

# # --- سیٹنگز (Settings) ---
# input_folder = r"C:\Users\PCS\Downloads\New folder"
# output_folder = os.path.join(input_folder, 'final_processed_thumbnails')
# os.makedirs(output_folder, exist_ok=True)

# # پہلے پروگرام کا رنگ (رنگ بدلنے کے لیے)
# content_hex_color = "#FFEFD5" 

# # دوسرے پروگرام کا کینوس کلر (بیک گراؤنڈ کے لیے)
# canvas_bg_color = (245, 230, 205) 

# # تھمب نیل سائز
# thumb_width, thumb_height = 1200, 800
# blur_radius = 25
# shadow_opacity = 90
# shadow_offset = (15, 15)

# def hex_to_bgr(hex_str):
#     hex_str = hex_str.lstrip('#')
#     rgb = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
#     return np.array([rgb[2], rgb[1], rgb[0]], dtype=np.float32)

# def process_images():
#     target_color_bgr = hex_to_bgr(content_hex_color)
#     counter = 1

#     print("Processing started...")

#     for filename in os.listdir(input_folder):
#         if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#             img_path = os.path.join(input_folder, filename)
            
#             # --- مرحلہ 1: OpenCV کے ذریعے رنگ تبدیل کرنا ---
#             cv_img = cv2.imread(img_path)
#             if cv_img is None: continue

#             # امیج کو فلوٹ میں بدل کر کلر اپلائی کرنا
#             img_float = cv_img.astype(np.float32) / 255.0
#             colored_img = img_float * target_color_bgr
#             colored_img = np.clip(colored_img, 0, 255).astype(np.uint8)

#             # OpenCV (BGR) کو PIL (RGBA) میں تبدیل کریں
#             colored_img_rgb = cv2.cvtColor(colored_img, cv2.COLOR_BGR2RGB)
#             pil_img = Image.fromarray(colored_img_rgb).convert("RGBA")

#             # --- مرحلہ 2: PIL کے ذریعے تھمب نیل بنانا ---
            
#             # کنٹراسٹ بہتر کریں
#             enhancer = ImageEnhance.Contrast(pil_img.convert("RGB"))
#             pil_img = enhancer.enhance(1.1).convert("RGBA")

#             # ری سائز (85% Height)
#             max_h = int(thumb_height * 0.85)
#             pil_img.thumbnail((thumb_width, max_h), Image.LANCZOS)

#             # پوزیشن کیلکولیٹ کریں
#             x = (thumb_width - pil_img.width) // 2
#             y = (thumb_height - pil_img.height) // 2

#             # ڈراپ شیڈو (Drop Shadow) بنانا
#             shadow_canvas = Image.new("RGBA", (pil_img.width + blur_radius * 2, pil_img.height + blur_radius * 2), (0, 0, 0, 0))
#             shadow_draw = ImageDraw.Draw(shadow_canvas)
#             shadow_draw.rectangle(
#                 [blur_radius, blur_radius, pil_img.width + blur_radius, pil_img.height + blur_radius], 
#                 fill=(0, 0, 0, shadow_opacity)
#             )
#             shadow_canvas = shadow_canvas.filter(ImageFilter.GaussianBlur(blur_radius))

#             # فائنل کینوس بنانا
#             final_thumb = Image.new("RGB", (thumb_width, thumb_height), canvas_bg_color)
            
#             # پہلے شیڈو پیسٹ کریں پھر مین امیج
#             final_thumb.paste(shadow_canvas, (x + shadow_offset[0] - blur_radius, y + shadow_offset[1] - blur_radius), shadow_canvas)
#             final_thumb.paste(pil_img, (x, y), pil_img)

#             # --- مرحلہ 3: سیو کرنا ---
#             custom_name = f"www.urdunovelbanks.com({counter}).webp"
#             save_path = os.path.join(output_folder, custom_name)
#             final_thumb.save(save_path, format="WEBP", optimize=True, quality=90)

#             print(f"Done: {custom_name}")
#             counter += 1

#     print(f"\n✔️ تمام {counter-1} تصاویر کامیابی سے تیار ہو چکی ہیں!")

# if __name__ == "__main__":
#     process_images()













# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# v3
# import os
# from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFilter

# # 📁 Folders
# input_folder = r"C:\Users\PCS\Downloads\New folder"
# output_folder = os.path.join(input_folder, 'canva_style_thumbnails')
# os.makedirs(output_folder, exist_ok=True)

# # 🎯 Canvas Settings
# thumb_width, thumb_height = 1200, 800
# bg_color = (248, 235, 215)  # Background cream color

# # 🌑 Canva Shadow Settings
# shadow_blur = 30      # Canva Blur amount: 30
# shadow_intensity = 128# Canva Intensity 50% (255 ka half)
# shadow_spread = 10   # Canva Size: 15

# # 🔁 Process Images
# counter = 1
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         img_path = os.path.join(input_folder, filename)
        
#         try:
#             # 1. Open Image
#             raw_img = Image.open(img_path).convert("RGB")

#             # 2. Cover Color Change (Image ko cream tint dena)
#             # Hum image ko thora sepia/cream look den ge jesa sample me hai
#             img = ImageOps.colorize(ImageOps.grayscale(raw_img), black="#3e2723", white="#f5e6cb")
#             img = ImageEnhance.Contrast(img).enhance(1.1)

#             # 3. Resize
#             max_h = int(thumb_height * 0.82)
#             img.thumbnail((thumb_width, max_h), Image.LANCZOS)
#             img_w, img_h = img.size

#             # 4. Create Shadow (Canva Style Backdrop)
#             # Spread ki wajha se shadow image se thora bara hota hai
#             shadow_w, shadow_h = img_w + (shadow_spread * 2), img_h + (shadow_spread * 2)
#             shadow = Image.new("RGBA", (shadow_w, shadow_h), (0, 0, 0, 0))
#             draw = ImageDraw.Draw(shadow)
#             draw.rectangle([0, 0, shadow_w, shadow_h], fill=(0, 0, 0, shadow_intensity))
#             shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))

#             # 5. Composite Final Image
#             final_thumb = Image.new("RGB", (thumb_width, thumb_height), bg_color)
            
#             # Center positions
#             x = (thumb_width - img_w) // 2
#             y = (thumb_height - img_h) // 2
            
#             # Paste Shadow (centered behind image)
#             shadow_x = (thumb_width - shadow_w) // 2
#             shadow_y = (thumb_height - shadow_h) // 2
#             final_thumb.paste(shadow, (shadow_x, shadow_y), shadow)
            
#             # Paste Image
#             final_thumb.paste(img, (x, y))

#             # 6. Save
#             save_path = os.path.join(output_folder, f"www.urdunovelbanks.com({counter}).webp")
#             final_thumb.save(save_path, "WEBP", quality=90)
            
#             print(f"Done: {filename} -> {counter}")
#             counter += 1

#         except Exception as e:
#             print(f"Error on {filename}: {e}")

# print(f"\n✅ Done! Check folder: {output_folder}")













#v2
# import os
# import math
# from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# # 📁 Input & Output folders
# input_folder = r"C:\Users\PCS\Downloads\New folder"
# output_folder = os.path.join(input_folder, 'thumbnails_final_v2')
# os.makedirs(output_folder, exist_ok=True)

# # 🧹 Clean output folder: delete all files except .webp
# for f in os.listdir(output_folder):
#     if not f.lower().endswith('.webp'):
#         try:
#             os.remove(os.path.join(output_folder, f))
#         except:
#             pass

# # 🎯 Canvas size (Landscape)
# thumb_width = 1200
# thumb_height = 800
# thumb_size = (thumb_width, thumb_height)

# # 🎨 Target Background Color (Light Beige/Cream, like reference image 2)
# bg_color = (250, 240, 230)

# # 🌑 Soft Drop Shadow settings
# blur_radius = 30
# shadow_opacity = 100 # 0-255
# shadow_offset = (10, 10) # Slight offset to the bottom-right

# # 🔁 Process all images
# counter = 1
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         img_path = os.path.join(input_folder, filename)
        
#         try:
#             # Open and Convert
#             img = Image.open(img_path).convert("RGBA")

#             # 🔧 Resize image to fit well within the canvas
#             max_h = int(thumb_height * 0.85)
#             max_w = int(thumb_width * 0.85)
#             img.thumbnail((max_w, max_h), Image.LANCZOS)

#             # 🎯 Center position for the image
#             img_x = (thumb_width - img.width) // 2
#             img_y = (thumb_height - img.height) // 2

#             # ☁️ Create soft drop shadow
#             # Create a larger canvas for blur
#             shadow_canvas = Image.new("RGBA", (thumb_width + blur_radius*2, thumb_height + blur_radius*2), (0, 0, 0, 0))
#             shadow_draw = ImageDraw.Draw(shadow_canvas)
#             # Draw the shadow rectangle
#             shadow_draw.rectangle(
#                 [img_x + shadow_offset[0], img_y + shadow_offset[1], img_x + img.width + shadow_offset[0], img_y + img.height + shadow_offset[1]],
#                 fill=(0, 0, 0, shadow_opacity)
#             )
#             # Apply blur
#             shadow_canvas = shadow_canvas.filter(ImageFilter.GaussianBlur(blur_radius))
#             # Crop shadow back to thumbnail size
#             shadow_final = shadow_canvas.crop((0, 0, thumb_width, thumb_height))

#             # 🖼 Create final composite image
#             final_thumb = Image.new("RGB", thumb_size, bg_color)
            
#             # Paste Shadow first
#             final_thumb.paste(shadow_final, (0, 0), shadow_final)
            
#             # Paste Main Image on top
#             final_thumb.paste(img, (img_x, img_y), img)

#             # 💾 Save as .webp
#             custom_name = f"www.urdunovelbanks.com({counter}).webp"
#             output_path = os.path.join(output_folder, custom_name)
#             final_thumb.save(output_path, format="WEBP", optimize=True, quality=90)

#             print(f"Generated: {custom_name}")
#             counter += 1

#         except Exception as e:
#             print(f"Error processing {filename}: {e}")

# print(f"\n✔️ Tamam thumbnails '{output_folder}' mein target design ke mutabiq generate ho chuki hain.")


#v1

# import os
# import math
# from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# # 📁 Input & Output folders
# input_folder = r"C:\Users\PCS\Downloads\New folder"
# output_folder = os.path.join(input_folder, 'thumbnails_final')
# os.makedirs(output_folder, exist_ok=True)

# # 🧹 Clean output folder: delete all files except .webp
# for f in os.listdir(output_folder):
#     if not f.lower().endswith('.webp'):
#         try:
#             os.remove(os.path.join(output_folder, f))
#         except:
#             pass

# # 🎯 Canvas size (Landscape)
# thumb_width = 1200
# thumb_height = 800
# thumb_size = (thumb_width, thumb_height)

# # 🎨 Target Background Color (دوسری تصویر جیسا کریم رنگ)
# bg_color = (245, 230, 205) # Specific Beige Color

# # 🌑 Drop shadow settings
# blur_radius = 25
# opacity = 90  # Soft shadow
# shadow_color = (0, 0, 0, opacity)
# offset = (15, 15) # Shadow slightly to the bottom-right

# # 🔁 Process all images
# counter = 1
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         img_path = os.path.join(input_folder, filename)
        
#         # Open and Convert
#         img = Image.open(img_path).convert("RGBA")

#         # 🎨 Enhance image (Thora contrast aur brightness behtar karne k liye)
#         enhancer = ImageEnhance.Contrast(img.convert("RGB"))
#         img = enhancer.enhance(1.1).convert("RGBA")

#         # 🔧 Resize image to fit (Vertical style like the sample)
#         # Hum image ko canvas ki height ka 85% tak rakhen gey
#         max_h = int(thumb_height * 0.85)
#         img.thumbnail((thumb_width, max_h), Image.LANCZOS)

#         # 🎯 Center position
#         x = (thumb_width - img.width) // 2
#         y = (thumb_height - img.height) // 2

#         # ☁️ Create drop shadow
#         # Shadow canvas image se thora bara hona chahiye blur k liye
#         shadow_canvas = Image.new("RGBA", (img.width + blur_radius * 2, img.height + blur_radius * 2), (0, 0, 0, 0))
#         shadow_draw = ImageDraw.Draw(shadow_canvas)
#         shadow_draw.rectangle([blur_radius, blur_radius, img.width + blur_radius, img.height + blur_radius], fill=shadow_color)
#         shadow_canvas = shadow_canvas.filter(ImageFilter.GaussianBlur(blur_radius))

#         # 🖼 Create final composite image
#         final_thumb = Image.new("RGB", thumb_size, bg_color)
        
#         # Paste Shadow
#         final_thumb.paste(shadow_canvas, (x + offset[0] - blur_radius, y + offset[1] - blur_radius), shadow_canvas)
        
#         # Paste Main Image
#         final_thumb.paste(img, (x, y), img)

#         # 💾 Save as .webp
#         custom_name = f"www.urdunovelbanks.com({counter}).webp"
#         output_path = os.path.join(output_folder, custom_name)
#         final_thumb.save(output_path, format="WEBP", optimize=True, quality=90)

#         print(f"Generated: {custom_name}")
#         counter += 1

# print("\n✔️ Mubarak ho! Tamam thumbnails target design k mutabiq generate ho chuki hain.")