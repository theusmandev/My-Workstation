from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import os
import sys

# -------------------------------
# Config
# -------------------------------
POEMS = [
    "یہ عشق نہیں آساں\nبس اتنا سمجھ لیجے\nایک آگ کا دریا ہے",
    "دل کی بات دل ہی جانے\nلفظوں میں چھپانے کی کوشش نہ کرو",
]

OUTPUT_DIR = r"E:\SUNB\urdu poetry bank\thumbnails"
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630
FONT_PATH = r"E:\SUNB\urdu poetry bank\NotoNastaliqUrdu-VariableFont_wght.ttf"
FALLBACK_FONT_PATH = r"E:\SUNB\urdu poetry bank\NotoNastaliqUrdu-VariableFont_wght.ttf" # Replace with valid path
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
    try:
        bbox = font.getbbox(text)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        if width == 0 or height == 0:
            print(f"Warning: Text '{text}' produced invalid dimensions (width={width}, height={height})")
            return 0, 0
        return width, height
    except Exception as e:
        print(f"Error calculating text dimensions for '{text}': {e}")
        return 0, 0

# -------------------------------
# Function to load font with fallback
# -------------------------------
def load_font(font_path, size):
    """Load a font with a fallback option."""
    for path in [font_path, FALLBACK_FONT_PATH]:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, size)
                print(f"Font loaded successfully: {path}")
                # Test rendering a sample Urdu character
                test_width, test_height = get_text_dimensions("یہ", font)
                if test_width > 0 and test_height > 0:
                    return font
                else:
                    print(f"Font at {path} does not support Urdu characters")
            except IOError as e:
                print(f"Failed to load font at {path}: {e}")
        else:
            print(f"Font file not found: {path}")
    print("Error: No valid Urdu font found. Please install a working Urdu font.")
    print("Suggestion: Download 'Noto Nastaliq Urdu' from https://fonts.google.com/noto/specimen/Noto+Nastaliq+Urdu")
    return None

# -------------------------------
# Function to render poetry
# -------------------------------
def create_thumbnail(poem_text, output_path):
    try:
        # Shape Urdu text
        print(f"Original poem: {poem_text}")
        reshaped_text = arabic_reshaper.reshape(poem_text)
        bidi_text = get_display(reshaped_text)
        print(f"Reshaped and bidi text: {bidi_text}")

        # Create image
        img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color=BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        # Load fonts
        font = load_font(FONT_PATH, FONT_SIZE)
        watermark_font = load_font(FONT_PATH, WATERMARK_SIZE)
        if not font or not watermark_font:
            print("Cannot create thumbnail: No valid font available")
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
                if w_width == 0:
                    print(f"Skipping unrenderable text: {test_line}")
                    continue
                if w_width <= max_width:
                    cur_line = test_line
                else:
                    lines.append(cur_line)
                    cur_line = w
            if cur_line:
                lines.append(cur_line)
        print(f"Wrapped lines: {lines}")

        if not lines:
            print("Error: No valid lines to render")
            return

        # Calculate vertical position
        total_height = sum([get_text_dimensions(l, font)[1] for l in lines]) + (len(lines)-1)*LINE_SPACING
        y = (IMAGE_HEIGHT - total_height) // 2

        # Draw each line
        for line in lines:
            w, h = get_text_dimensions(line, font)
            if w == 0 or h == 0:
                print(f"Skipping unrenderable line: {line}")
                continue
            x = (IMAGE_WIDTH - w) // 2
            draw.text((x, y), line, fill=TEXT_COLOR, font=font)
            y += h + LINE_SPACING

        # Draw watermark
        wm_w, wm_h = get_text_dimensions(WATERMARK_TEXT, watermark_font)
        if wm_w > 0 and wm_h > 0:
            draw.text((IMAGE_WIDTH - wm_w - 20, IMAGE_HEIGHT - wm_h - 20),
                      WATERMARK_TEXT, fill=(180,180,180), font=watermark_font)
        else:
            print("Warning: Watermark text could not be rendered")

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
    print(f"Output directory created: {OUTPUT_DIR}")
except OSError as e:
    print(f"Error: Could not create directory {OUTPUT_DIR}: {e}")
    sys.exit(1)

for i, poem in enumerate(POEMS, 1):
    out_file = os.path.join(OUTPUT_DIR, f"poem_{i}.png")
    create_thumbnail(poem, out_file)