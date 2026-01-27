from PIL import ImageFont
import os

FONT_PATH = r"E:\SUNB\urdu poetry bank\NotoNastaliqUrdu-VariableFont_wght.ttf"

print("File exists?", os.path.exists(FONT_PATH))

try:
    font = ImageFont.truetype(FONT_PATH, 40)
    print("✅ Font loaded successfully!")
except Exception as e:
    print("❌ Font load error:", e)
