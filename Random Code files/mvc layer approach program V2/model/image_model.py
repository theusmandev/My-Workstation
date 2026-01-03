from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter, ImageFont
import math

class ThumbnailModel:
    def __init__(self, watermark_text="www.urdunovelbanks.com", font_path=None):
        self.watermark_text = watermark_text
        self.font_path = font_path

    # Enhance image
    def enhance_image(self, img):
        img = ImageEnhance.Color(img).enhance(1.3)
        img = ImageEnhance.Brightness(img).enhance(1.1)
        img = ImageEnhance.Contrast(img).enhance(1.25)
        return img

    # Get average color
    def average_color(self, img):
        stat = ImageStat.Stat(img)
        return tuple(int(c) for c in stat.mean[:3])

    # Create vertical watermark (bottom to top)
    def create_vertical_watermark(self, bg_color):
        from PIL import ImageFont, ImageDraw, Image
        r, g, b = bg_color
        luminance = (0.299*r + 0.587*g + 0.114*b)/255
        text_color = (0,0,0,255) if luminance > 0.5 else (255,255,255,255)
        try:
            font = ImageFont.truetype(self.font_path, 26) if self.font_path else ImageFont.load_default()
        except:
            font = ImageFont.load_default()
        padding = 30
        temp = Image.new("RGBA", (200,200))
        draw = ImageDraw.Draw(temp)
        try:
            bbox = draw.textbbox((0,0), self.watermark_text, font=font)
            text_w = bbox[2]-bbox[0]
            text_h = bbox[3]-bbox[1]
        except:
            text_w, text_h = font.getsize(self.watermark_text)
        text_img = Image.new("RGBA", (text_w+padding, text_h+padding), (0,0,0,0))
        draw = ImageDraw.Draw(text_img)
        draw.text((padding//2,padding//2), self.watermark_text, font=font, fill=text_color)
        return text_img.rotate(90, expand=True)
