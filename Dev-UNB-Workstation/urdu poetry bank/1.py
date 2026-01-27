from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

# Urdu text sample
text = "یہ عشق نہیں آساں\nبس اتنا سمجھ لیجے\nایک آگ کا دریا ہے"

# Proper shaping for Urdu text
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)

# Image setup (white background)
img = Image.new("RGB", (800, 600), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# ✅ Font path (make sure this path is correct on your system)
font = ImageFont.truetype(
    r"E:\SUNB\urdu poetry bank\NotoNastaliqUrdu-Regular.ttf", 
    40
)

# Draw text (black color)
draw.text((50, 200), bidi_text, font=font, fill=(0, 0, 0))

# ✅ Save image (fixed file name)
output_path = r"E:\SUNB\urdu poetry bank\poetry_test.png"
img.save(output_path)

print(f"✅ Image saved successfully: {output_path}")
