import cairocffi as cairo
import uharfbuzz as hb
import os

# ---------------------------
# Config
# ---------------------------
FONT_PATH = r"E:\SUNB\urdu poetry bank\JameelNooriNastaleeq.ttf"  # static TTF
OUTPUT_DIR = r"E:\SUNB\urdu poetry bank\thumbnails"
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630
FONT_SIZE = 60
BACKGROUND_COLOR = (0.1, 0.1, 0.1)  # Dark gray background (0-1)
TEXT_COLOR = (1, 1, 1)  # White (0-1)
WATERMARK = "Urdu Poetry Bank"
WATERMARK_SIZE = 30

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------
# Helper: render Urdu text
# ---------------------------
def render_urdu_to_surface(text, output_path):
    # Load font
    with open(FONT_PATH, "rb") as fontfile:
        fontdata = fontfile.read()
    face = hb.Face(fontdata)
    font = hb.Font(face)

    # Create Cairo surface
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, IMAGE_WIDTH, IMAGE_HEIGHT)
    ctx = cairo.Context(surface)

    # Fill background
    ctx.set_source_rgb(*BACKGROUND_COLOR)
    ctx.rectangle(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT)
    ctx.fill()

    # Initialize HarfBuzz buffer
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)

    # Get glyph info
    infos = buf.glyph_infos
    positions = buf.glyph_positions

    # Draw text
    ctx.set_source_rgb(*TEXT_COLOR)
    ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(FONT_SIZE)

    x, y = 50, IMAGE_HEIGHT // 2
    for info, pos in zip(infos, positions):
        gid = info.codepoint
        x_offset = pos.x_offset / 64
        y_offset = pos.y_offset / 64
        x_advance = pos.x_advance / 64
        y_advance = pos.y_advance / 64
        ctx.move_to(x + x_offset, y - y_offset)
        ctx.show_glyphs([cairo.Glyph(gid, x, y)])
        x += x_advance
        y += y_advance

    # Watermark
    ctx.set_font_size(WATERMARK_SIZE)
    ctx.move_to(IMAGE_WIDTH - 300, IMAGE_HEIGHT - 50)
    ctx.show_text(WATERMARK)

    # Save
    surface.write_to_png(output_path)
    print(f"✅ Saved: {output_path}")

# ---------------------------
# Example Usage
# ---------------------------
poems = [
    "یہ عشق نہیں آساں\nبس اتنا سمجھ لیجے\nایک آگ کا دریا ہے",
    "دل کی بات دل ہی جانے\nلفظوں میں چھپانے کی کوشش نہ کرو",
]

for i, poem in enumerate(poems, 1):
    out_file = os.path.join(OUTPUT_DIR, f"poem_{i}.png")
    render_urdu_to_surface(poem, out_file)
