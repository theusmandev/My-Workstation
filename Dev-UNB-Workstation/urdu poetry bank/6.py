import os
from PIL import Image, ImageDraw, ImageFont  # ✅ Add ImageFont
import freetype
import arabic_reshaper
from bidi.algorithm import get_display


# -------------------------------
# Config
# -------------------------------
POEMS = [
    "یہ عشق نہیں آساں\nبس اتنا سمجھ لیجے\nایک آگ کا دریا ہے",
    "دل کی بات دل ہی جانے\nلفظوں میں چھپانے کی کوشش نہ کرو",
]

OUTPUT_DIR = r"E:\SUNB\urdu poetry bank\thumbnails"
os.makedirs(OUTPUT_DIR, exist_ok=True)

IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630
FONT_PATH = r"E:\SUNB\urdu poetry bank\NotoNastaliqUrdu-Medium.ttf"
FONT_SIZE = 50
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (30, 30, 30)
WATERMARK_TEXT = "Urdu Poetry Bank"
WATERMARK_SIZE = 30

# -------------------------------
# Helper: draw text with freetype
# -------------------------------
def draw_text(image, text, font_path, font_size, pos):
    import freetype
    face = freetype.Face(font_path)
    face.set_char_size(font_size*64)
    x, y = pos
    for char in text:
        face.load_char(char)
        bitmap = face.glyph.bitmap
        top = face.glyph.bitmap_top
        left = face.glyph.bitmap_left
        w, h = bitmap.width, bitmap.rows
        if w > 0 and h > 0:
            glyph_bytes = bytes(bitmap.buffer)  # <-- convert to bytes
            glyph_img = Image.frombytes('L', (w,h), glyph_bytes)
            # Convert grayscale to RGB
            rgb_glyph = Image.merge('RGB', (glyph_img, glyph_img, glyph_img))
            image.paste(rgb_glyph, (x+left, y-top+h), mask=glyph_img)
        x += face.glyph.advance.x >> 6


# -------------------------------
# Generate thumbnails
# -------------------------------
for idx, poem in enumerate(POEMS,1):
    img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color=BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Urdu shaping
    reshaped_text = arabic_reshaper.reshape(poem)
    bidi_text = get_display(reshaped_text)

    # Split lines
    lines = bidi_text.split('\n')
    total_height = len(lines)*(FONT_SIZE+10)
    y = (IMAGE_HEIGHT - total_height)//2

    # Draw each line
    for line in lines:
        bbox = draw.textbbox((0,0), line, font=None)
        w = bbox[2] - bbox[0]
        x = (IMAGE_WIDTH - w)//2
        draw_text(img, line, FONT_PATH, FONT_SIZE, (x, y))
        y += FONT_SIZE + 10

    # Draw watermark using Pillow (simpler)
    watermark_font = ImageFont.truetype(FONT_PATH, WATERMARK_SIZE)
    wm_bbox = draw.textbbox((0,0), WATERMARK_TEXT, font=watermark_font)
    wm_w = wm_bbox[2] - wm_bbox[0]
    wm_h = wm_bbox[3] - wm_bbox[1]
    draw.text((IMAGE_WIDTH - wm_w - 20, IMAGE_HEIGHT - wm_h - 20),
              WATERMARK_TEXT, fill=(180,180,180), font=watermark_font)

    out_path = os.path.join(OUTPUT_DIR, f"poem_{idx}.png")
    img.save(out_path)
    print(f"✅ Saved: {out_path}")
