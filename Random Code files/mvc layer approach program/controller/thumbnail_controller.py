# controller/thumbnail_controller.py
import os
from PIL import Image
from model.image_model import ThumbnailModel
from view.console_view import ConsoleView

class ThumbnailController:

    def __init__(self, input_folder, output_folder, font_path):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.model = ThumbnailModel(
            font_path,
            "www.urdunovelbanks.com"
        )
        os.makedirs(output_folder, exist_ok=True)

    def process(self):
        count = 1
        for file in os.listdir(self.input_folder):
            if not file.lower().endswith(('.jpg','.png','.jpeg','.webp')):
                continue

            img = Image.open(os.path.join(self.input_folder, file)).convert("RGB")
            img = self.model.enhance_image(img)

            avg = self.model.average_color(img)
            bg = Image.new("RGB", (1200,800), avg)

            img.thumbnail((600,720))
            x = (1200-img.width)//2
            y = (800-img.height)//2

            composite = bg.convert("RGBA")
            shadow = self.model.create_shadow(img.size)

            composite.paste(shadow, (x-20, y+20), shadow)
            img = img.convert("RGBA")
            composite.paste(img, (x, y), img)


            watermark = self.model.create_vertical_watermark(avg)
            composite.alpha_composite(
                watermark,
                (x+img.width+15, y)
            )

            out_name = f"www.urdunovelbanks.com({count}).webp"
            out_path = os.path.join(self.output_folder, out_name)
            composite.convert("RGB").save(out_path, "WEBP", quality=88)

            ConsoleView.show_generated(out_name)
            count += 1

        ConsoleView.done(count-1, self.output_folder)
