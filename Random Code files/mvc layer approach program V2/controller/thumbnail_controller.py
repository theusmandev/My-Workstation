import os
from PIL import Image, ImageDraw, ImageFilter
from model.image_model import ThumbnailModel

class ThumbnailController:
    def __init__(self, input_folder, output_folder, font_path=None, view=None):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.model = ThumbnailModel(font_path=font_path)
        self.view = view
        os.makedirs(self.output_folder, exist_ok=True)

    def process(self):
        counter = 1
        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith((".jpg",".jpeg",".png",".webp")):
                img_path = os.path.join(self.input_folder, filename)
                try:
                    img = Image.open(img_path).convert("RGB")
                except:
                    continue

                img = self.model.enhance_image(img)
                avg_color = self.model.average_color(img)

                # Background + composite
                thumb_size = (1200,800)
                background = Image.new("RGB", thumb_size, avg_color)
                composite = background.convert("RGBA")

                # Resize image
                max_w, max_h = int(thumb_size[0]*0.5), int(thumb_size[1]*0.9)
                img.thumbnail((max_w,max_h), Image.LANCZOS)
                x = (thumb_size[0]-img.width)//2
                y = (thumb_size[1]-img.height)//2

                # Shadow
                shadow_color = (0,0,0,128)
                shadow = Image.new("RGBA", img.size, shadow_color)
                shadow = shadow.filter(ImageFilter.GaussianBlur(20))
                x_offset, y_offset = -30, 30
                composite.paste(shadow, (x+x_offset, y+y_offset), shadow)

                # Paste image
                img = img.convert("RGBA")
                composite.paste(img, (x,y), img)

                # Watermark
                watermark = self.model.create_vertical_watermark(avg_color)
                wm_x = x + img.width + 18
                wm_y = y + (img.height - watermark.height)//2
                if wm_x + watermark.width > thumb_size[0]:
                    wm_x = thumb_size[0] - watermark.width - 12
                composite.alpha_composite(watermark, (wm_x, wm_y))

                # Save
                out_name = f"www.urdunovelbanks.com({counter}).webp"
                out_path = os.path.join(self.output_folder, out_name)
                composite.convert("RGB").save(out_path, "WEBP", optimize=True, quality=88)
                if self.view:
                    self.view.show_generated(out_name)
                counter += 1
        if self.view:
            self.view.done(counter-1, self.output_folder)
