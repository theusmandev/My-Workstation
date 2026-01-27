from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import os

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
FONT_PATH = r"E:\SUNB\urdu poetry bank\NotoNastaliqUrdu-Medium.ttf" # static TTF
FONT_SIZE = 50
TEXT_COLOR = (255, 255, 255)  # white
BACKGROUND_COLOR = (30, 30, 30)  # dark gray
WATERMARK_TEXT = "Urdu Poetry Bank"
WATERMARK_SIZE = 30

# -------------------------------
# Function to render poetry
# -------------------------------
def create_thumbnail(poem_text, output_path):
    # Shape Urdu text
    reshaped_text = arabic_reshaper.reshape(poem_text)
    bidi_text = get_display(reshaped_text)

    # Create image
    img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color=BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    watermark_font = ImageFont.truetype(FONT_PATH, WATERMARK_SIZE)

    # Auto wrap lines
    max_width = IMAGE_WIDTH - 100
    lines = []
    for line in bidi_text.split('\n'):
        words = line.split(' ')
        cur_line = ""
        for w in words:
            test_line = cur_line + " " + w if cur_line else w
            bbox = draw.textbbox((0,0), test_line, font=font)
            w_width = bbox[2] - bbox[0]
            if w_width <= max_width:
                cur_line = test_line
            else:
                lines.append(cur_line)
                cur_line = w
        if cur_line:
            lines.append(cur_line)

    # Calculate vertical position
    line_heights = [draw.textbbox((0,0), l, font=font)[3] - draw.textbbox((0,0), l, font=font)[1] for l in lines]
    total_height = sum(line_heights) + (len(lines)-1)*10
    y = (IMAGE_HEIGHT - total_height)//2

    # Draw each line center aligned
    for line, h in zip(lines, line_heights):
        bbox = draw.textbbox((0,0), line, font=font)
        w = bbox[2] - bbox[0]
        x = (IMAGE_WIDTH - w)//2
        draw.text((x, y), line, fill=TEXT_COLOR, font=font)
        y += h + 10

    # Draw watermark
    wm_bbox = draw.textbbox((0,0), WATERMARK_TEXT, font=watermark_font)
    wm_w = wm_bbox[2] - wm_bbox[0]
    wm_h = wm_bbox[3] - wm_bbox[1]
    draw.text((IMAGE_WIDTH - wm_w - 20, IMAGE_HEIGHT - wm_h - 20),
              WATERMARK_TEXT, fill=(180,180,180), font=watermark_font)

    # Save image
    img.save(output_path)
    print(f"✅ Saved: {output_path}")

# -------------------------------
# Generate thumbnails
# -------------------------------
for i, poem in enumerate(POEMS, 1):
    out_file = os.path.join(OUTPUT_DIR, f"poem_{i}.png")
    create_thumbnail(poem, out_file)
