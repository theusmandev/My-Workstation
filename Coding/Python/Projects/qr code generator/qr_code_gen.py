import qrcode
import os
from pathlib import Path

class ProfessionalQRGenerator:
    def __init__(self, save_directory):
        # Hard-coded path ko set karna
        self.save_path = Path(save_directory)
        
        # Agar folder maujood nahi hai to usay create karna
        if not self.save_path.exists():
            self.save_path.mkdir(parents=True, exist_ok=True)
            print(f"Directory created: {self.save_path}")

    def create_qr(self, link, file_name, folder_name="MyQRCodes"):
        try:
            # QR Code ki settings (Professional Grade)
            qr = qrcode.QRCode(
                version=3,  # QR ka complexity level
                error_correction=qrcode.constants.ERROR_CORRECT_H, # High Error Correction (Logo lagane ke liye best)
                box_size=15, # Quality behtar karne ke liye pixels barhaye hain
                border=4,
            )
            
            qr.add_data(link)
            qr.make(fit=True)

            # Color customization (Professional look: Dark Blue on White)
            img = qr.make_image(fill_color="#1a237e", back_color="white")

            # Full path generate karna
            full_path = self.save_path / f"{file_name}.png"
            
            # File save karna
            img.save(full_path)
            print(f"--- SUCCESS ---")
            print(f"QR Code Saved at: {full_path}")
            
        except Exception as e:
            print(f"Error: {e}")

# --- CONFIGURATION (Yahan apna path aur link set karein) ---

# Hard-coded path jahan aap files save karna chahte hain
# Windows example: "C:/Users/Name/Desktop/MyQRs"
# Mac/Linux example: "/home/user/documents/qrcodes"
SAVE_DIR = r"E:\My-Workstation\Coding\Python\Projects\qr code generator\QR CODES"

# Website ya data ka link
TARGET_LINK = "https://www.google.com"
FILE_NAME = "google_professional_qr"

# Generator ko run karna
if __name__ == "__main__":
    generator = ProfessionalQRGenerator(SAVE_DIR)
    generator.create_qr(TARGET_LINK, FILE_NAME)