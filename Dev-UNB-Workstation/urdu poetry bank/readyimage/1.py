from PIL import Image, ImageDraw, ImageFont
import os

# -------------------------------
# Config
# -------------------------------
THUMB_WIDTH = 1200
THUMB_HEIGHT = 630
BACKGROUND_COLOR = (30, 30, 30)  # Dark grey background

POEM_IMAGE_PATH = r"C:\Users\PCS\Downloads\1758910477204.png" # Transparent Urdu PNG
OUTPUT_FOLDER = r"E:\SUNB\urdu poetry bank\thumbnails"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "final_thumbnail.png")

# Watermark
WATERMARK_TEXT = "Urdu Poetry Bank"
WATERMARK_SIZE = 30
WATERMARK_COLOR = (180, 180, 180)  # light grey

# -------------------------------
# Load background
# -------------------------------
thumbnail = Image.new("RGB", (THUMB_WIDTH, THUMB_HEIGHT), color=BACKGROUND_COLOR)

# -------------------------------
# Load transparent poem image
# -------------------------------
poem_img = Image.open(POEM_IMAGE_PATH).convert("RGBA")

# Resize poem image if too big
max_width = THUMB_WIDTH - 100
max_height = THUMB_HEIGHT - 150  # leave space for watermark
poem_ratio = poem_img.width / poem_img.height

if poem_img.width > max_width or poem_img.height > max_height:
    if poem_ratio > 1:  # width dominant
        new_width = max_width
        new_height = int(max_width / poem_ratio)
    else:  # height dominant
        new_height = max_height
        new_width = int(max_height * poem_ratio)
    poem_img = poem_img.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)

# -------------------------------
# Paste poem image centered
# -------------------------------
poem_x = (THUMB_WIDTH - poem_img.width) // 2-100
poem_y = (THUMB_HEIGHT - poem_img.height - 50) // 2  # leave bottom space for watermark
thumbnail.paste(poem_img, (poem_x, poem_y), mask=poem_img)

# -------------------------------
# Add watermark
# -------------------------------
draw = ImageDraw.Draw(thumbnail)
# Use default PIL font (no need for Urdu font)
font = ImageFont.load_default()

# Calculate watermark size using textbbox
bbox = draw.textbbox((0, 0), WATERMARK_TEXT, font=font)
wm_w = bbox[2] - bbox[0]
wm_h = bbox[3] - bbox[1]

draw.text(
    ((THUMB_WIDTH - wm_w) // 2, THUMB_HEIGHT - wm_h - 20),
    WATERMARK_TEXT,
    font=font,
    fill=WATERMARK_COLOR
)

# -------------------------------
# Save final thumbnail
# -------------------------------
thumbnail.save(OUTPUT_FILE)
print(f"✅ Final thumbnail saved: {OUTPUT_FILE}")
