
"""
enhancer.enhance(1.3) ka matlab hai saturation 30% zyada.

ImageOps.expand(..., border=20) ka matlab hai 20 pixels ka black border.

Ye script sari .png, .jpg, .jpeg, aur .webp files par apply hogi.
"""

# import os
# from PIL import Image, ImageEnhance, ImageOps

# # 📁 Input folder jahan images mojood hain
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"

# # 📁 Output folder (same as input or different if you want)
# output_folder = os.path.join(input_folder, 'edited_images')
# os.makedirs(output_folder, exist_ok=True)

# # 🔄 Loop through all images
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert('RGB')

#         # 🎨 1. Saturation increase
#         enhancer = ImageEnhance.Color(img)
#         saturated_img = enhancer.enhance(1.3)  # 1.0 = original, >1 = more saturated

#         # 🔲 2. Add black border
#         bordered_img = ImageOps.expand(saturated_img, border=20, fill='black')

#         # 💾 Save edited image
#         output_path = os.path.join(output_folder, filename)
#         bordered_img.save(output_path)

# print("✔️ Saari images process ho chuki hain aur save ho gayi hain:", output_folder)







#not worked as intended

# import os
# from PIL import Image, ImageEnhance, ImageOps

# # 📁 Input folder jahan images mojood hain
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"

# # 📁 Output folder
# output_folder = os.path.join(input_folder, 'edited_images')
# os.makedirs(output_folder, exist_ok=True)

# # 📏 Desired output size (standard)
# standard_width = 600
# standard_height = 800

# # 🔄 Loop through all images
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert('RGB')

#         # 🎨 1. Saturation increase
#         enhancer = ImageEnhance.Color(img)
#         img = enhancer.enhance(1.3)

#         # 💡 2. Brightness adjustment
#         bright = ImageEnhance.Brightness(img)
#         img = bright.enhance(1.1)

#         # 🌑 3. Contrast adjustment
#         contrast = ImageEnhance.Contrast(img)
#         img = contrast.enhance(1.2)

#         # 🖼 4. Resize while maintaining aspect ratio (no crop)
#         img.thumbnail((standard_width, standard_height), Image.LANCZOS)

#         # 🔲 5. Add black border (after resizing)
#         bordered_img = ImageOps.expand(img, border=20, fill='black')

#         # 💾 Save edited image
#         output_path = os.path.join(output_folder, filename)
#         bordered_img.save(output_path, optimize=True, quality=85)  # Web optimized

# print("✔️ Saari images process ho chuki hain aur save ho gayi hain:", output_folder)



'''
Har image exactly 600x800 pixels ki hogi.

Image ka aspect ratio preserve hoga.

Agar image chhoti ho to black padding apply hogi.

Border bhi separately diya gaya hai (20 pixels).
'''


# import os
# from PIL import Image, ImageEnhance, ImageOps

# # 📁 Input folder jahan images mojood hain
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"

# # 📁 Output folder
# output_folder = os.path.join(input_folder, 'edited_images')
# os.makedirs(output_folder, exist_ok=True)

# # 📏 Desired output canvas size
# canvas_size = (600, 800)

# # 🔄 Loop through all images
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert('RGB')

#         # 🎨 1. Saturation increase
#         img = ImageEnhance.Color(img).enhance(1.3)

#         # 💡 2. Brightness adjustment
#         img = ImageEnhance.Brightness(img).enhance(1.1)

#         # 🌑 3. Contrast adjustment
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🖼 4. Resize + pad to canvas size without changing ratio
#         padded_img = ImageOps.pad(img, canvas_size, method=Image.LANCZOS, color='black', centering=(0.5, 0.5))

#         # 🔲 5. Add extra black border (optional)
#         final_img = ImageOps.expand(padded_img, border=20, fill='black')

#         # 💾 Save edited image
#         output_path = os.path.join(output_folder, filename)
#         final_img.save(output_path, optimize=True, quality=85)

# print("✔️ Saari images process ho chuki hain aur save ho gayi hain:", output_folder)










# import os
# from PIL import Image, ImageEnhance, ImageOps, ImageStat

# # 📁 Input folder jahan images mojood hain
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"

# # 📁 Output folder
# output_folder = os.path.join(input_folder, 'edited_images')
# os.makedirs(output_folder, exist_ok=True)

# # 🔲 Border size (in pixels)
# border_size = 13

# # 🔄 Loop through all images
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert('RGB')

#         # 🎨 1. Saturation increase
#         img = ImageEnhance.Color(img).enhance(1.3)

#         # 💡 2. Brightness adjustment
#         img = ImageEnhance.Brightness(img).enhance(1.1)

#         # 🌑 3. Contrast adjustment
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🎯 4. Automatically detect average color from image
#         stat = ImageStat.Stat(img)
#         avg_color = tuple(int(c) for c in stat.mean)  # e.g., (R, G, B)

#         # 🔲 5. Add border using that color
#         bordered_img = ImageOps.expand(img, border=border_size, fill=avg_color)

#         # 💾 Save image
#         output_path = os.path.join(output_folder, filename)
#         bordered_img.save(output_path, optimize=True, quality=85)

# print("✔️ Saari images process ho chuki hain aur save ho gayi hain:", output_folder)











'''
Image ko 100x100 par resize kiya jata hai taake fast color analysis ho.

getcolors() se (count, color) pairs milte hain.

max(..., key=lambda x: x[0]) ka matlab: jo color sabse zyada repeat hua usay select karo.
'''




# import os
# from PIL import Image, ImageEnhance, ImageOps

# # 📁 Input folder
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"

# # 📁 Output folder
# output_folder = os.path.join(input_folder, 'edited_images')
# os.makedirs(output_folder, exist_ok=True)

# # 🔲 Border size
# border_size = 13

# # 🔄 Process each image
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert('RGB')

#         # 🎨 Saturation
#         img = ImageEnhance.Color(img).enhance(1.3)

#         # 💡 Brightness
#         img = ImageEnhance.Brightness(img).enhance(1.1)

#         # 🌑 Contrast
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🎯 Dominant color detection
#         small_img = img.resize((100, 100))  # Resize for faster processing
#         colors = small_img.getcolors(10000)  # (count, color)
#         dominant_color = max(colors, key=lambda x: x[0])[1]

#         # 🔲 Add border with dominant color
#         bordered_img = ImageOps.expand(img, border=border_size, fill=dominant_color)

#         # 💾 Save image
#         output_path = os.path.join(output_folder, filename)
#         bordered_img.save(output_path, optimize=True, quality=85)

# print("✔️ Saari images process ho chuki hain aur save ho gayi hain:", output_folder)






'''
Border color ab bhi average color par based hai ✅

Lekin uska saturation ab 1.8× tak enhance kiya gaya hai ✅

Zyada attractive aur novel-style pop-out borders milenge 🎯
'''





# import os
# from PIL import Image, ImageEnhance, ImageOps, ImageStat
# import colorsys

# # 📁 Input folder
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"

# # 📁 Output folder
# output_folder = os.path.join(input_folder, 'edited_images')
# os.makedirs(output_folder, exist_ok=True)

# # 🔲 Border size
# border_size = 13

# # 🔄 Process each image
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert('RGB')

#         # 🎨 Saturation
#         img = ImageEnhance.Color(img).enhance(1.3)

#         # 💡 Brightness
#         img = ImageEnhance.Brightness(img).enhance(1.1)

#         # 🌑 Contrast
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🎯 Average color
#         stat = ImageStat.Stat(img)
#         avg_color = tuple(int(c) for c in stat.mean[:3])  # RGB

#         # 🎨 Convert to HSV to enhance saturation
#         r, g, b = [x / 255.0 for x in avg_color]
#         h, s, v = colorsys.rgb_to_hsv(r, g, b)
#         s = min(1.0, s * 1.8)  # Increase saturation (max 1.0)
#         r_sat, g_sat, b_sat = colorsys.hsv_to_rgb(h, s, v)
#         saturated_color = tuple(int(x * 255) for x in (r_sat, g_sat, b_sat))

#         # 🔲 Add border with saturated color
#         bordered_img = ImageOps.expand(img, border=border_size, fill=saturated_color)

#         # 💾 Save
#         output_path = os.path.join(output_folder, filename)
#         bordered_img.save(output_path, optimize=True, quality=85)

# print("✔️ Saari images process ho chuki hain aur save ho gayi hain:", output_folder)




'''
Har novel image ab center mein hogi

Background ka rang image ka average color hoga

Novel ke neeche soft shadow hoga (like a book on a table)

Size exactly 1000x667 px hoga (SEO aur web ke liye perfect)
'''


# import os
# from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# # 📁 Input folder
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"
# output_folder = os.path.join(input_folder, 'thumbnails_1000x667')
# os.makedirs(output_folder, exist_ok=True)

# # 🎯 Thumbnail canvas size
# thumb_width = 1000
# thumb_height = 667
# thumb_size = (thumb_width, thumb_height)

# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert("RGB")

#         # 📌 Enhancement
#         img = ImageEnhance.Color(img).enhance(1.3)
#         img = ImageEnhance.Brightness(img).enhance(1.1)
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🎯 Average color for background
#         stat = ImageStat.Stat(img)
#         avg_color = tuple(int(c) for c in stat.mean[:3])

#         # 🖼 Create thumbnail background
#         background = Image.new("RGB", thumb_size, avg_color)

#         # 🔄 Resize cover image to fit inside 70% of thumbnail size
#         max_cover_width = int(thumb_width * 0.5)
#         max_cover_height = int(thumb_height * 0.9)
#         img.thumbnail((max_cover_width, max_cover_height), Image.LANCZOS)

#         # 📏 Calculate position to center
#         x = (thumb_width - img.width) // 2
#         y = (thumb_height - img.height) // 2

#         # ☁️ Create shadow
#         shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
#         shadow_draw = ImageDraw.Draw(shadow)
#         shadow_draw.rectangle([0, 0, img.width, img.height], fill=(0, 0, 0, 80))
#         shadow = shadow.filter(ImageFilter.GaussianBlur(10))

#         # 📌 Paste shadow on background (slightly offset)
#         background_with_shadow = background.convert("RGBA")
#         background_with_shadow.paste(shadow, (x+5, y+5), shadow)

#         # 📌 Paste image on top
#         background_with_shadow.paste(img, (x, y))

#         # 💾 Save final image
#         final_image = background_with_shadow.convert("RGB")
#         output_path = os.path.join(output_folder, filename)
#         final_image.save(output_path, optimize=True, quality=85)

# print("✔️ Thumbnails (1000x667) tayar ho gayi hain:", output_folder)












'''
 Output Preview:
Novel cover is centered ✅

Drop shadow applied at 37° angle ✅

Shadow color = Black with 50% opacity ✅

Shadow is softly blurred to look natural ✅

Background is image's average color ✅

Final size = 1000x667 ✅
'''




# import os
# import math
# from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# # 📁 Input & Output
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"
# output_folder = os.path.join(input_folder, 'thumbnails_1000x667')
# os.makedirs(output_folder, exist_ok=True)

# # 🎯 Canvas size
# thumb_width = 1000
# thumb_height = 667
# thumb_size = (thumb_width, thumb_height)

# # 🌑 Drop shadow settings
# angle_degrees = 37
# distance = 10  # distance of shadow from image
# opacity = 128  # 0 to 255 (128 = ~50%)
# shadow_color = (0, 0, 0, opacity)

# # Compute x, y offset based on angle
# angle_radians = math.radians(angle_degrees)
# x_offset = int(distance * math.cos(angle_radians))
# y_offset = int(distance * math.sin(angle_radians))

# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert("RGB")

#         # 🎨 Enhance
#         img = ImageEnhance.Color(img).enhance(1.3)
#         img = ImageEnhance.Brightness(img).enhance(1.1)
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🎯 Background color
#         stat = ImageStat.Stat(img)
#         avg_color = tuple(int(c) for c in stat.mean[:3])
#         background = Image.new("RGB", thumb_size, avg_color)

#         # 🔄 Resize novel image
#         max_cover_width = int(thumb_width * 0.5)
#         max_cover_height = int(thumb_height * 0.9)
#         img.thumbnail((max_cover_width, max_cover_height), Image.LANCZOS)

#         # 📍 Positioning
#         x = (thumb_width - img.width) // 2
#         y = (thumb_height - img.height) // 2

#         # ☁️ Create shadow
#         shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
#         draw = ImageDraw.Draw(shadow)
#         draw.rectangle([0, 0, img.width, img.height], fill=shadow_color)
#         shadow = shadow.filter(ImageFilter.GaussianBlur(8))  # Blur for realism

#         # 🖼 Composite: add shadow first with offset
#         composite = background.convert("RGBA")
#         composite.paste(shadow, (x + x_offset, y + y_offset), shadow)

#         # 🖼 Then add actual image
#         composite.paste(img, (x, y))

#         # 💾 Save
#         final_image = composite.convert("RGB")
#         output_path = os.path.join(output_folder, filename)
#         final_image.save(output_path, optimize=True, quality=85)

# print("✔️ Drop shadow thumbnails ready at:", output_folder)


'''

Feature	Value
Canvas Size	1000x667 px
Shadow Angle	37° (left-down direction)
Shadow Opacity	50% (RGBA 128)                      OKKOKOKOK
Shadow Color	Black
Background Color	Image ka average RGB color
Novel Cover	Centered with enhancements
'''



# import os
# import math
# from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# # 📁 Input & Output folders
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"
# output_folder = os.path.join(input_folder, 'thumbnails_1000x667')
# os.makedirs(output_folder, exist_ok=True)

# # 🎯 Canvas size
# thumb_width = 1000
# thumb_height = 667
# thumb_size = (thumb_width, thumb_height)

# # 🌑 Drop shadow settings
# angle_degrees = 37
# distance = 10  # distance of shadow from image
# opacity = 128  # 0 to 255 (128 = ~50% opacity)
# shadow_color = (0, 0, 0, opacity)

# # ➖ ➕ Compute left-side offset from angle
# angle_radians = math.radians(angle_degrees)
# x_offset = -int(distance * math.cos(angle_radians))   # ← left side
# y_offset = int(distance * math.sin(angle_radians))    # ↓ downward

# # 🔄 Process all images
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert("RGB")

#         # 🎨 Enhance image
#         img = ImageEnhance.Color(img).enhance(1.3)
#         img = ImageEnhance.Brightness(img).enhance(1.1)
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🎯 Get average color from image for background
#         stat = ImageStat.Stat(img)
#         avg_color = tuple(int(c) for c in stat.mean[:3])
#         background = Image.new("RGB", thumb_size, avg_color)

#         # 🔄 Resize novel image to fit nicely
#         max_cover_width = int(thumb_width * 0.5)
#         max_cover_height = int(thumb_height * 0.9)
#         img.thumbnail((max_cover_width, max_cover_height), Image.LANCZOS)

#         # 📍 Position image at center
#         x = (thumb_width - img.width) // 2
#         y = (thumb_height - img.height) // 2

#         # ☁️ Create soft drop shadow with blur
#         shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
#         draw = ImageDraw.Draw(shadow)
#         draw.rectangle([0, 0, img.width, img.height], fill=shadow_color)
#         shadow = shadow.filter(ImageFilter.GaussianBlur(8))

#         # 🖼 Add shadow first with offset (left side)
#         composite = background.convert("RGBA")
#         composite.paste(shadow, (x + x_offset, y + y_offset), shadow)

#         # 🖼 Paste original image
#         composite.paste(img, (x, y))

#         # 💾 Save final image
#         final_image = composite.convert("RGB")
#         output_path = os.path.join(output_folder, filename)
#         final_image.save(output_path, optimize=True, quality=85)

# print("✔️ Saari thumbnails ready hain (1000x667, left drop shadow):", output_folder)






















# import os
# import math
# from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# # 📁 Input & Output folders
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"
# output_folder = os.path.join(input_folder, 'thumbnails_1000x667')
# os.makedirs(output_folder, exist_ok=True)

# # 🎯 Canvas size
# thumb_width = 1000
# thumb_height = 667
# thumb_size = (thumb_width, thumb_height)

# # 🌑 Drop shadow settings (From Canva)
# angle_degrees = 37
# distance = 30        # Canva setting
# blur_radius = 20       # Canva blur
# opacity = 128          # 50% opacity
# shadow_color = (0, 0, 0, opacity)  # Black with alpha

# # ➖ ➕ Compute offset for angle
# angle_radians = math.radians(angle_degrees)
# x_offset = -int(distance * math.cos(angle_radians))   # Left side
# y_offset = int(distance * math.sin(angle_radians))    # Downward

# # 🔄 Process images
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert("RGB")

#         # 📌 Enhance
#         img = ImageEnhance.Color(img).enhance(1.3)
#         img = ImageEnhance.Brightness(img).enhance(1.1)
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🎯 Background (based on average color)
#         stat = ImageStat.Stat(img)
#         avg_color = tuple(int(c) for c in stat.mean[:3])
#         background = Image.new("RGB", thumb_size, avg_color)

#         # 🔄 Resize novel cover
#         max_cover_width = int(thumb_width * 0.5)
#         max_cover_height = int(thumb_height * 0.9)
#         img.thumbnail((max_cover_width, max_cover_height), Image.LANCZOS)

#         # 🧭 Center position
#         x = (thumb_width - img.width) // 2
#         y = (thumb_height - img.height) // 2

#         # ☁️ Shadow layer
#         shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
#         draw = ImageDraw.Draw(shadow)
#         draw.rectangle([0, 0, img.width, img.height], fill=shadow_color)
#         shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))

#         # 🖼 Composite image: background + shadow + cover
#         composite = background.convert("RGBA")
#         composite.paste(shadow, (x + x_offset, y + y_offset), shadow)
#         composite.paste(img, (x, y))

#         # 💾 Save final thumbnail
#         final_image = composite.convert("RGB")
#         output_path = os.path.join(output_folder, filename)
#         final_image.save(output_path, optimize=True, quality=85)

# print("✔️ Thumbnails (1000x667) with Canva-style left shadow tayar hain:", output_folder)






'''Output format: .webp

File name pattern: www.urdunovelbanks.com(1).webp, www.urdunovelbanks.com(2).webp, etc.'''






# import os
# import math
# from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# # 📁 Input & Output folders
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"
# output_folder = os.path.join(input_folder, 'thumbnails_1000x667')
# os.makedirs(output_folder, exist_ok=True)

# # 🎯 Canvas size
# thumb_width = 1000
# thumb_height = 667
# thumb_size = (thumb_width, thumb_height)

# # 🌑 Drop shadow settings (From Canva)
# angle_degrees = 37
# distance = 30           # Updated distance
# blur_radius = 20        # Canva blur
# opacity = 128           # 50% opacity
# shadow_color = (0, 0, 0, opacity)  # Black with alpha

# # ➖ ➕ Compute offset for angle
# angle_radians = math.radians(angle_degrees)
# x_offset = -int(distance * math.cos(angle_radians))   # Left
# y_offset = int(distance * math.sin(angle_radians))    # Down

# # 🔄 Process images
# counter = 1
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         img_path = os.path.join(input_folder, filename)
#         img = Image.open(img_path).convert("RGB")

#         # 🎨 Enhance
#         img = ImageEnhance.Color(img).enhance(1.3)
#         img = ImageEnhance.Brightness(img).enhance(1.1)
#         img = ImageEnhance.Contrast(img).enhance(1.2)

#         # 🎯 Average color for background
#         stat = ImageStat.Stat(img)
#         avg_color = tuple(int(c) for c in stat.mean[:3])
#         background = Image.new("RGB", thumb_size, avg_color)

#         # 📐 Resize novel image
#         max_cover_width = int(thumb_width * 0.5)
#         max_cover_height = int(thumb_height * 0.9)
#         img.thumbnail((max_cover_width, max_cover_height), Image.LANCZOS)

#         # 🧭 Center position
#         x = (thumb_width - img.width) // 2
#         y = (thumb_height - img.height) // 2

#         # ☁️ Create shadow
#         shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
#         draw = ImageDraw.Draw(shadow)
#         draw.rectangle([0, 0, img.width, img.height], fill=shadow_color)
#         shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))

#         # 🖼 Composite image
#         composite = background.convert("RGBA")
#         composite.paste(shadow, (x + x_offset, y + y_offset), shadow)
#         composite.paste(img, (x, y))

#         # 💾 Save as .webp with custom filename
#         final_image = composite.convert("RGB")
#         custom_name = f"www.urdunovelbanks.com({counter}).webp"
#         output_path = os.path.join(output_folder, custom_name)
#         final_image.save(output_path, format="WEBP", optimize=True, quality=85)

#         counter += 1

# print("✔️ WEBP thumbnails tayar ho gayi hain:", output_folder)







# import os
# import math
# from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# # 📁 Input & Output folders
# input_folder = r"C:\Users\PCS\Downloads\unb\imgs"
# output_folder = os.path.join(input_folder, 'thumbnails_1000x667')
# os.makedirs(output_folder, exist_ok=True)

# # 📏 Thumbnail canvas size
# thumb_width = 1000
# thumb_height = 667
# thumb_size = (thumb_width, thumb_height)

# # 🌑 Drop shadow settings (based on Canva)
# angle_degrees = 37
# distance = 30
# blur_radius = 20
# opacity = 128  # 50% opacity
# shadow_color = (0, 0, 0, opacity)  # Black with alpha

# # 🔢 Compute x, y offset for shadow
# angle_radians = math.radians(angle_degrees)
# x_offset = -int(distance * math.cos(angle_radians))  # Left
# y_offset = int(distance * math.sin(angle_radians))   # Down

# # 🔄 Process all images
# counter = 1
# for filename in os.listdir(input_folder):
#     if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
#         continue  # Skip unsupported files

#     img_path = os.path.join(input_folder, filename)
#     img = Image.open(img_path).convert("RGB")

#     # 🎨 Enhance image
#     img = ImageEnhance.Color(img).enhance(1.3)
#     img = ImageEnhance.Brightness(img).enhance(1.1)
#     img = ImageEnhance.Contrast(img).enhance(1.2)

#     # 🎯 Average color for background
#     stat = ImageStat.Stat(img)
#     avg_color = tuple(int(c) for c in stat.mean[:3])
#     background = Image.new("RGB", thumb_size, avg_color)

#     # 📐 Resize novel cover to fit
#     max_cover_width = int(thumb_width * 0.5)
#     max_cover_height = int(thumb_height * 0.9)
#     img.thumbnail((max_cover_width, max_cover_height), Image.LANCZOS)

#     # 🧭 Center position
#     x = (thumb_width - img.width) // 2
#     y = (thumb_height - img.height) // 2

#     # ☁️ Create shadow
#     shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
#     draw = ImageDraw.Draw(shadow)
#     draw.rectangle([0, 0, img.width, img.height], fill=shadow_color)
#     shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))

#     # 🖼 Combine: background + shadow + image
#     composite = background.convert("RGBA")
#     composite.paste(shadow, (x + x_offset, y + y_offset), shadow)
#     composite.paste(img, (x, y))

#     # 💾 Save as .webp with custom name
#     final_image = composite.convert("RGB")
#     custom_name = f"www.urdunovelbanks.com({counter}).webp"
#     output_path = os.path.join(output_folder, custom_name)
#     final_image.save(output_path, format="WEBP", optimize=True, quality=85)

#     counter += 1

# print("✔️ Saari thumbnails `.webp` format mein generate ho chuki hain:", output_folder)




















import os
import math
from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter

# 📁 Input & Output folders
input_folder = r"E:\SUNB\Writers All Novels\Farhat istiaq png"
output_folder = os.path.join(input_folder, 'thumbnails_1000x667')
os.makedirs(output_folder, exist_ok=True)

# 🧹 Clean output folder: delete all files except .webp
for f in os.listdir(output_folder):
    if not f.lower().endswith('.webp'):
        os.remove(os.path.join(output_folder, f))

# 🎯 Canvas size
thumb_width = 1000
thumb_height = 667
thumb_size = (thumb_width, thumb_height)

# 🌑 Drop shadow settings (Canva-style)
angle_degrees = 37
distance = 30
blur_radius = 20
opacity = 128  # 50% opacity
shadow_color = (0, 0, 0, opacity)  # Black with alpha

# ➕➖ Shadow offset based on angle
angle_radians = math.radians(angle_degrees)
x_offset = -int(distance * math.cos(angle_radians))   # Left
y_offset = int(distance * math.sin(angle_radians))    # Down

# 🔁 Process all images
counter = 1
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB")

        # 🎨 Enhance image
        img = ImageEnhance.Color(img).enhance(1.3)
        img = ImageEnhance.Brightness(img).enhance(1.1)
        img = ImageEnhance.Contrast(img).enhance(1.2)

        # 🎯 Get average background color
        stat = ImageStat.Stat(img)
        avg_color = tuple(int(c) for c in stat.mean[:3])
        background = Image.new("RGB", thumb_size, avg_color)

        # 🔧 Resize image to fit in thumbnail
        max_cover_width = int(thumb_width * 0.5)
        max_cover_height = int(thumb_height * 0.9)
        img.thumbnail((max_cover_width, max_cover_height), Image.LANCZOS)

        # 🎯 Center position
        x = (thumb_width - img.width) // 2
        y = (thumb_height - img.height) // 2

        # ☁️ Create drop shadow
        shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(shadow)
        draw.rectangle([0, 0, img.width, img.height], fill=shadow_color)
        shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))

        # 🖼 Create final composite image
        composite = background.convert("RGBA")
        composite.paste(shadow, (x + x_offset, y + y_offset), shadow)
        composite.paste(img, (x, y))

        # 💾 Save as .webp with custom name
        final_image = composite.convert("RGB")
        custom_name = f"www.urdunovelbanks.com({counter}).webp"
        output_path = os.path.join(output_folder, custom_name)
        final_image.save(output_path, format="WEBP", optimize=True, quality=85)

        counter += 1

print("✔️ Sirf WEBP thumbnails successfully generate ho chuki hain:", output_folder)
