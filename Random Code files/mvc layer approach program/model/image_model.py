# model/image_model.py
import math
from PIL import Image, ImageEnhance, ImageStat, ImageDraw, ImageFilter, ImageFont

class ThumbnailModel:

    def __init__(self, font_path, watermark_text):
        self.watermark_text = watermark_text
        try:
            self.font = ImageFont.truetype(font_path, 26)
        except:
            self.font = ImageFont.load_default()

    def enhance_image(self, img):
        img = ImageEnhance.Color(img).enhance(1.3)
        img = ImageEnhance.Brightness(img).enhance(1.1)
        img = ImageEnhance.Contrast(img).enhance(1.25)
        return img

    def average_color(self, img):
        stat = ImageStat.Stat(img)
        return tuple(int(c) for c in stat.mean[:3])

    def best_text_color(self, bg):
        r, g, b = bg
        luminance = (0.299*r + 0.587*g + 0.114*b)/255
        return (0,0,0,255) if luminance > 0.5 else (255,255,255,255)

    def create_vertical_watermark(self, bg_color):
        color = self.best_text_color(bg_color)
        temp = Image.new("RGBA", (400, 100))
        d = ImageDraw.Draw(temp)
        bbox = d.textbbox((0,0), self.watermark_text, font=self.font)
        w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]

        img = Image.new("RGBA", (w+30, h+30), (0,0,0,0))
        draw = ImageDraw.Draw(img)
        draw.text((15,15), self.watermark_text, font=self.font, fill=color)

        return img.rotate(90, expand=True)

    def create_shadow(self, size):
        shadow = Image.new("RGBA", size, (0,0,0,128))
        return shadow.filter(ImageFilter.GaussianBlur(20))
