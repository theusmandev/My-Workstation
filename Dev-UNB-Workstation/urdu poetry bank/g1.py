from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import os

# -------------------------------
# Config
# -------------------------------
POEMS = [
    "یہ عشق نہیں آساں\nبس اتنا سمجھ لیجے\nاusman",
    "دل کی بات دل ہی جانے\nلفظوں میں چھپانے کی کوشش نہ کرو",
]

OUTPUT_DIR = r"E:\SUNB\urdu poetry bank\thumbnails"
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630
FONT_PATH = r"E:\SUNB\urdu poetry bank\NotoNastaliqUrdu-Medium.ttf"
FONT_SIZE = 50
TEXT_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (30, 30, 30)  # Dark gray
WATERMARK_TEXT = "Urdu Poetry Bank"
WATERMARK_SIZE = 30
LINE_SPACING = 10

# -------------------------------
# Helper function to get text dimensions
# -------------------------------
def get_text_dimensions(text, font):
    """Calculate text width and height using font.getbbox."""
    bbox = font.getbbox(text)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height

# -------------------------------
# Function to render poetry
# -------------------------------
def create_thumbnail(poem_text, output_path):
    try:
        # Shape Urdu text
        reshaped_text = arabic_reshaper.reshape(poem_text)
        bidi_text = get_display(reshaped_text)

        # Create image
        img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color=BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        # Load font
        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
            watermark_font = ImageFont.truetype(FONT_PATH, WATERMARK_SIZE)
        except IOError:
            print(f"Error: Font file not found at {FONT_PATH}")
            return

        # Auto wrap lines
        max_width = IMAGE_WIDTH - 100
        lines = []
        for line in bidi_text.split('\n'):
            words = line.split(' ')
            cur_line = ""
            for w in words:
                test_line = cur_line + " " + w if cur_line else w
                w_width, _ = get_text_dimensions(test_line, font)
                if w_width <= max_width:
                    cur_line = test_line
                else:
                    lines.append(cur_line)
                    cur_line = w
            if cur_line:
                lines.append(cur_line)

        # Calculate vertical position
        total_height = sum([get_text_dimensions(l, font)[1] for l in lines]) + (len(lines)-1)*LINE_SPACING
        y = (IMAGE_HEIGHT - total_height) // 2

        # Draw each line
        for line in lines:
            w, h = get_text_dimensions(line, font)
            x = (IMAGE_WIDTH - w) // 2
            draw.text((x, y), line, fill=TEXT_COLOR, font=font)
            y += h + LINE_SPACING

        # Draw watermark
        wm_w, wm_h = get_text_dimensions(WATERMARK_TEXT, watermark_font)
        draw.text((IMAGE_WIDTH - wm_w - 20, IMAGE_HEIGHT - wm_h - 20),
                  WATERMARK_TEXT, fill=(180,180,180), font=watermark_font)

        # Save image
        img.save(output_path)
        print(f"✅ Saved: {output_path}")

    except Exception as e:
        print(f"Error creating thumbnail for {output_path}: {e}")

# -------------------------------
# Generate thumbnails
# -------------------------------
try:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
except OSError as e:
    print(f"Error: Could not create directory {OUTPUT_DIR}: {e}")
    exit(1)

for i, poem in enumerate(POEMS, 1):
    out_file = os.path.join(OUTPUT_DIR, f"poem_{i}.png")
    create_thumbnail(poem, out_file)