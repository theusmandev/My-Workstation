"""
Urdu Poetry Thumbnail Generator
Requirements:
  pip install Pillow arabic-reshaper python-bidi

Usage:
  - Provide a path to a Nastaleeq .ttf font.
  - Call create_thumbnail(text, font_path, out_path, **options)
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
import os

# Optional libraries for proper Arabic/Urdu shaping
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    HAS_SHAPING = True
except Exception:
    HAS_SHAPING = False

def shape_urdu(text: str) -> str:
    """Apply Arabic reshaper and bidi to render Urdu correctly."""
    if not HAS_SHAPING:
        return text
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)
    return bidi_text

def wrap_text_for_width(text, font, draw, max_width):
    """
    Wrap text so its rendered width <= max_width.
    Returns list of lines (already shaped if shaping is available).
    """
    # Use simple word-wrapping using spaces. For Urdu it generally works.
    words = text.split()
    lines = []
    current = ""
    for w in words:
        test = (w if current == "" else current + " " + w)
        # shape for measuring (so measurement is accurate)
        shaped = shape_urdu(test)
        bbox = draw.textbbox((0,0), shaped, font=font)
        wpx = bbox[2] - bbox[0]
        if wpx <= max_width:
            current = test
        else:
            if current == "":
                # single word longer than width, force break
                lines.append(test)
                current = ""
            else:
                lines.append(current)
                current = w
    if current:
        lines.append(current)
    # Return shaped lines for drawing (reverse order so they visually RTL)
    shaped_lines = [shape_urdu(line) for line in lines]
    return shaped_lines

def create_gradient(size, start=(20,20,20), end=(60,60,60), horizontal=False):
    """Create simple two-color gradient background."""
    base = Image.new('RGB', size, start)
    top = Image.new('RGB', size, end)
    mask = Image.new('L', size)
    mask_data = []
    w, h = size
    if horizontal:
        for x in range(w):
            a = int(255 * (x / (w - 1)))
            mask_data.extend([a] * h)
    else:
        for y in range(h):
            a = int(255 * (y / (h - 1)))
            mask_data.extend([a] * w)
    mask.putdata(mask_data)
    base.paste(top, (0,0), mask)
    return base

def create_thumbnail(
    text,
    font_path,
    out_path,
    size=(1200, 630),
    background='black',   # 'black', 'white', 'gradient', or path to image (floral)
    gradient_colors=((20,20,20),(80,20,40)), # used if background == 'gradient'
    font_size=None,
    padding=60,
    watermark_text="Urdu Poetry Bank",
    watermark_font_size=None,
    watermark_opacity=150,  # 0-255
    watermark_margin=30,
    text_color=(255,255,255),
    save_format='PNG'
):
    # Prepare canvas
    W, H = size

    # Background handling
    if isinstance(background, str) and os.path.isfile(background):
        bg = Image.open(background).convert('RGB')
        bg = bg.resize((W, H), Image.LANCZOS)
    elif background == 'gradient':
        bg = create_gradient((W,H), start=gradient_colors[0], end=gradient_colors[1])
    elif background == 'white':
        bg = Image.new('RGB', (W,H), (255,255,255))
    else:
        # default black
        bg = Image.new('RGB', (W,H), (0,0,0))

    draw = ImageDraw.Draw(bg)

    # Load font
    if font_size is None:
        font_size = int(W * 0.06)  # heuristic
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        raise RuntimeError(f"Cannot load font at {font_path}: {e}")

    # Wrap text
    max_text_width = W - 2 * padding
    lines = wrap_text_for_width(text, font, draw, max_text_width)

    # Calculate total text height
    line_heights = []
    for line in lines:
        bbox = draw.textbbox((0,0), line, font=font)
        line_heights.append(bbox[3] - bbox[1])
    line_spacing = int(font_size * 0.2)
    total_text_height = sum(line_heights) + (len(lines)-1)*line_spacing

    # Starting y (center vertically)
    current_y = (H - total_text_height) // 2

    # Draw each line (centered)
    for line in lines:
        bbox = draw.textbbox((0,0), line, font=font)
        wpx = bbox[2] - bbox[0]
        # For Urdu (RTL), center align visually
        x = (W - wpx) // 2
        draw.text((x, current_y), line, font=font, fill=text_color)
        current_y += bbox[3] - bbox[1] + line_spacing

    # Watermark (semi-transparent)
    if watermark_font_size is None:
        watermark_font_size = max(14, int(W * 0.03))
    try:
        watermark_font = ImageFont.truetype(font_path, watermark_font_size)
    except Exception:
        watermark_font = ImageFont.load_default()

    wm_text_shaped = shape_urdu(watermark_text)
    wm_bbox = draw.textbbox((0,0), wm_text_shaped, font=watermark_font)
    wm_w = wm_bbox[2] - wm_bbox[0]
    wm_h = wm_bbox[3] - wm_bbox[1]

    # Create watermark layer with alpha
    watermark_layer = Image.new('RGBA', (W, H), (255,255,255,0))
    wm_draw = ImageDraw.Draw(watermark_layer)
    wm_x = W - wm_w - watermark_margin
    wm_y = H - wm_h - watermark_margin
    wm_draw.text((wm_x, wm_y), wm_text_shaped, font=watermark_font, fill=(255,255,255,watermark_opacity))

    # Optionally blur or style watermark (light)
    watermark_layer = watermark_layer.filter(ImageFilter.GaussianBlur(radius=0))

    combined = Image.alpha_composite(bg.convert('RGBA'), watermark_layer)

    # Save
    combined.convert('RGB').save(out_path, format=save_format)
    print(f"Saved thumbnail to: {out_path}")

# ----------------------------
# Example usage (uncomment and edit paths to run locally)
# ----------------------------
if __name__ == "__main__":
    sample_text = "یہ عشق نہیں آساں\nبس اتنا سمجھ لیجے\nایک آگ کا دریا ہے"
    FONT_PATH = r"E:\SUNB\urdu poetry bank\Jameel Noori Nastaleeq Kasheeda.ttf"   # <-- provide local path to .ttf
    OUT = r"E:\SUNB\urdu poetry bank\ok.png"
    create_thumbnail(
        text=sample_text,
        font_path=FONT_PATH,
        out_path=OUT,
        size=(1200,630),
        background='gradient',
        gradient_colors=((10,10,30),(60,10,30)),
        watermark_text="Urdu Poetry Bank",
        watermark_opacity=160
    )
