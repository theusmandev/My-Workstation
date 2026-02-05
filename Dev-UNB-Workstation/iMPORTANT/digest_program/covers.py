# from PIL import Image, ImageDraw, ImageFont

# # Cover size
# width, height = 600, 900
# cover = Image.new("RGB", (width, height), color=(255, 255, 240))  # ہلکا پیلا بیک گراؤنڈ

# draw = ImageDraw.Draw(cover)

# # Borders
# draw.rectangle([(20, 20), (width-20, height-20)], outline="darkred", width=8)

# # Fonts (اپنے PC کا کوئی فونٹ path دیں، مثلاً Jameel Noori Nastaleeq اردو کے لیے)
# title_font = ImageFont.truetype("arialbd.ttf", 60)   # بڑا ٹائٹل
# month_font = ImageFont.truetype("arial.ttf", 40)     # مہینہ اور سال

# # Title
# draw.text((100, 100), "Shua Digest", font=title_font, fill="darkred")

# # Month & Year
# draw.text((100, 200), "January 2000", font=month_font, fill="black")

# # Save Image
# cover.save("shua_digest_jan2000.jpg")



#Python Code (Centered Digest Cover on Background)


# from PIL import Image, ImageDraw, ImageFont

# # Background (canvas)
# canvas_width, canvas_height = 1000, 667
# canvas = Image.new("RGB", (canvas_width, canvas_height), color=(220, 220, 220))  # grey background

# # Digest cover size
# cover_width, cover_height = 400, 600
# cover = Image.new("RGB", (cover_width, cover_height), color=(255, 255, 240))  # light yellow cover

# draw = ImageDraw.Draw(cover)

# # Border for cover
# draw.rectangle([(10, 10), (cover_width-10, cover_height-10)], outline="darkred", width=6)

# # Fonts (آپ اردو فونٹ بھی لگا سکتے ہیں اگر installed ہو)
# title_font = ImageFont.truetype("arialbd.ttf", 40)
# month_font = ImageFont.truetype("arial.ttf", 28)

# # Add text on cover
# draw.text((50, 100), "Shua Digest", font=title_font, fill="darkred")
# draw.text((50, 180), "January 2000", font=month_font, fill="black")

# # Position cover at center of canvas
# x = (canvas_width - cover_width) // 2
# y = (canvas_height - cover_height) // 2

# # Paste cover on background
# canvas.paste(cover, (x, y))

# # Save final image
# canvas.save("digest_cover_centered.jpg")




#cover with shadow , googd ok okn


# from PIL import Image, ImageDraw, ImageFont

# # Background (canvas)
# canvas_width, canvas_height = 1000, 667
# canvas = Image.new("RGB", (canvas_width, canvas_height), color=(220, 220, 220))  # grey background

# # Digest cover size
# cover_width, cover_height = 400, 600
# cover = Image.new("RGB", (cover_width, cover_height), color=(255, 255, 240))  # light yellow cover

# draw = ImageDraw.Draw(cover)

# # Border for cover
# draw.rectangle([(10, 10), (cover_width-10, cover_height-10)], outline="darkred", width=6)

# # Fonts
# title_font = ImageFont.truetype("arialbd.ttf", 40)
# month_font = ImageFont.truetype("arial.ttf", 28)

# # Add text on cover
# draw.text((50, 100), "Shua Digest", font=title_font, fill="darkred")
# draw.text((50, 180), "January 2000", font=month_font, fill="black")

# # ---- Shadow effect ----
# shadow_offset = (10, 10)  # shadow ka shift
# shadow = cover.copy()
# shadow_draw = ImageDraw.Draw(shadow)
# shadow = shadow.convert("RGBA")

# # Pure black shadow with transparency
# shadow_layer = Image.new("RGBA", shadow.size, (0, 0, 0, 120))
# shadow.paste(shadow_layer, (0, 0), shadow_layer)

# # Positioning
# x = (canvas_width - cover_width) // 2
# y = (canvas_height - cover_height) // 2

# # Paste shadow first (slightly shifted)
# canvas.paste(shadow, (x + shadow_offset[0], y + shadow_offset[1]), shadow)

# # Paste real cover on top
# canvas.paste(cover, (x, y))

# # Save final image
# canvas.save("digest_cover_with_shadow.jpg")









from PIL import Image, ImageDraw, ImageFont

# Canvas
canvas_width, canvas_height = 1000, 667
canvas = Image.new("RGB", (canvas_width, canvas_height), color=(220, 220, 220))

# Cover
cover_width, cover_height = 400, 600
cover = Image.new("RGB", (cover_width, cover_height), color=(255, 255, 240))

draw = ImageDraw.Draw(cover)

# Border
draw.rectangle([(10, 10), (cover_width-10, cover_height-10)], outline="darkred", width=6)

# Fonts
title_font = ImageFont.truetype("arialbd.ttf", 45)
month_font = ImageFont.truetype("arial.ttf", 30)

# Title with shadow
draw.text((52, 102), "Shua Digest", font=title_font, fill="black")
draw.text((50, 100), "Shua Digest", font=title_font, fill="darkred")

draw.text((52, 182), "January 2000", font=month_font, fill="black")
draw.text((50, 180), "January 2000", font=month_font, fill="darkblue")

# ---- Bottom Design ----
design_height = 100
draw.rectangle([(0, cover_height-design_height), (cover_width, cover_height)], fill=(200, 50, 50))  # red strip

# Decorative diagonal lines
for i in range(0, cover_width, 40):
    draw.line([(i, cover_height-design_height), (i+50, cover_height)], fill="gold", width=3)

# Position at center of canvas
x = (canvas_width - cover_width) // 2
y = (canvas_height - cover_height) // 2

canvas.paste(cover, (x, y))

canvas.save("digest_cover_with_design.jpg")
