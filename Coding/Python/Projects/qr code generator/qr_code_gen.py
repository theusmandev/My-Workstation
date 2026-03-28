
import qrcode
import qrcode.image.svg
from pathlib import Path
from urllib.parse import urlparse

class UltimateQRGenerator:
    def __init__(self, save_directory):
        self.save_path = Path(save_directory)
        if not self.save_path.exists():
            self.save_path.mkdir(parents=True, exist_ok=True)
            print(f"Folder Created: {self.save_path}")

    def extract_name(self, url):
        parsed = urlparse(url)
        name = parsed.netloc.replace('www.', '')
        return name if name else "product_qr"

    def generate_dual(self, link):
        try:
            file_name = self.extract_name(link)
            
            # --- RESOLUTION SETTINGS ---
            # box_size=40 high quality 
            # version=1 best for short links
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=40,  # <--- change resolution here
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)

            # 1. PNG Generater  (High Resolution)
            img_png = qr.make_image(fill_color="black", back_color="white")
            png_path = self.save_path / f"{file_name}.png"
            img_png.save(png_path)

            # 2. SVG Generater(Professional Vector for Printing)
            factory = qrcode.image.svg.SvgPathImage
            img_svg = qr.make_image(image_factory=factory)
            svg_path = self.save_path / f"{file_name}.svg"
            img_svg.save(svg_path)

            print(f"--- SUCCESS ---")
            print(f"1. PNG Saved: {png_path} (High Res)")
            print(f"2. SVG Saved: {svg_path} (Printing Standard)")
            
        except Exception as e:
            print(f"Error: {e}")

# --- CONFIGURATION ---

SAVE_DIR = r"E:\My-Workstation\Coding\Python\Projects\qr code generator\QR CODES"
# Put your link here
TARGET_LINK = "https://maddentalcare.com/"

if __name__ == "__main__":
    generator = UltimateQRGenerator(SAVE_DIR)
    generator.generate_dual(TARGET_LINK)



# import qrcode
# import qrcode.image.svg
# import os
# from pathlib import Path
# from urllib.parse import urlparse
# import re

# class SerumQRManager:
#     def __init__(self, save_directory):
#         self.save_path = Path(save_directory)
#         self._ensure_directory()

#     def _ensure_directory(self):
#         """Check karna ke folder maujood hai ya nahi"""
#         try:
#             if not self.save_path.exists():
#                 self.save_path.mkdir(parents=True, exist_ok=True)
#                 print(f"[SYSTEM] Directory created: {self.save_path}")
#         except Exception as e:
#             print(f"[CRITICAL ERROR] Folder nahi ban saka: {e}")

#     def is_valid_url(self, url):
#         """Link ko check karna ke wo sahi format mein hai ya nahi"""
#         regex = re.compile(
#             r'^(?:http|ftp)s?://' # http:// ya https://
#             r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain
#             r'localhost|' # localhost
#             r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ip
#             r'(?::\d+)?' # port
#             r'(?:/?|[/?]\S+)$', re.IGNORECASE)
#         return re.match(regex, url) is not None

#     def extract_clean_name(self, url):
#         """Domain name nikalna file name ke liye"""
#         parsed = urlparse(url)
#         name = parsed.netloc.replace('www.', '')
#         return name if name else "generated_qr"

#     def generate(self, link, use_svg=True):
#         # 1. URL Validation
#         if not self.is_valid_url(link):
#             print(f"[ERROR] '{link}' aik valid link nahi hai. Please check karein.")
#             return

#         try:
#             file_name = self.extract_clean_name(link)
            
#             # QR Settings
#             qr = qrcode.QRCode(
#                 version=1, 
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 box_size=20, # High resolution
#                 border=4,
#             )
#             qr.add_data(link)
#             qr.make(fit=True)

#             if use_svg:
#                 # SVG Format (Best for Printing on Bottles)
#                 factory = qrcode.image.svg.SvgPathImage
#                 img = qr.make_image(image_factory=factory)
#                 extension = "svg"
#             else:
#                 # Standard PNG Format
#                 img = qr.make_image(fill_color="black", back_color="white")
#                 extension = "png"

#             full_path = self.save_path / f"{file_name}.{extension}"
            
#             # File save karna
#             with open(full_path, 'wb') as f:
#                 img.save(f)

#             print(f"--- SUCCESS ---")
#             print(f"File: {file_name}.{extension}")
#             print(f"Path: {full_path}")
#             print(f"Status: Ready for Printing")

#         except Exception as e:
#             print(f"[ERROR] QR Code nahi ban saka: {e}")

# # --- SETTINGS ---
# # Apna path yahan set karein
# MY_PATH = r"E:\My-Workstation\Coding\Python\Projects\qr code generator\QR CODES"
# MY_LINK = "https://cutdentalcare.com/" # Apna sahi link yahan dalein

# if __name__ == "__main__":
#     generator = SerumQRManager(MY_PATH)
#     # Generate SVG (Recommended for packaging)
#     generator.generate(MY_LINK, use_svg=True)










# import qrcode
# import os
# from pathlib import Path
# from urllib.parse import urlparse

# class ProfessionalQRGenerator:
#     def __init__(self, save_directory):
#         # Hard-coded path setup
#         self.save_path = Path(save_directory)
        
#         # Folder create karna agar maujood nahi hai
#         if not self.save_path.exists():
#             self.save_path.mkdir(parents=True, exist_ok=True)
#             print(f"Directory Created: {self.save_path}")

#     def extract_domain(self, url):
#         """Link mein se domain name nikalne ke liye logic"""
#         parsed_url = urlparse(url)
#         domain = parsed_url.netloc
#         # Agar link mein 'www.' hai to usay hata dena taake file name saaf ho
#         if domain.startswith('www.'):
#             domain = domain[4:]
#         return domain if domain else "qr_code"

#     def create_qr(self, link):
#         try:
#             # Domain name ko file name banana
#             file_name = self.extract_domain(link)
            
#             # QR Code Settings
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 box_size=50,
#                 border=4,
#             )
            
#             qr.add_data(link)
#             qr.make(fit=True)

#             # Pure Black and White style
#             img = qr.make_image(fill_color="black", back_color="white")

#             # Final Path (Filename automatic domain se banega)
#             full_path = self.save_path / f"{file_name}.png"
            
#             # Save the file
#             img.save(full_path)
            
#             print(f"--- SUCCESS ---")
#             print(f"Link: {link}")
#             print(f"File Saved As: {file_name}.png")
#             print(f"Location: {full_path}")
            
#         except Exception as e:
#             print(f"Error occurred: {e}")

# # --- CONFIGURATION ---

# # Aapka hard-coded path
# SAVE_DIR = r"E:\My-Workstation\Coding\Python\Projects\qr code generator\QR CODES"

# # Aapki product ka link (e.g. Teeth Whitening Serum page)
# TARGET_LINK = "https://cutdentalcare.com/" 

# # Run the generator
# if __name__ == "__main__":
#     generator = ProfessionalQRGenerator(SAVE_DIR)
#     generator.create_qr(TARGET_LINK)