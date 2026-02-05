import easyocr
import os

input_folder = r'C:\Users\PCS\Downloads\unb\New folder (4)ok'
output_folder = r'C:\Users\PCS\Downloads\unb\New folder (4)okokokokokocr'
os.makedirs(output_folder, exist_ok=True)

reader = easyocr.Reader(['ur'])  # 'ur' = Urdu

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)
        result = reader.readtext(image_path, detail=0, paragraph=True)
        text = "\n".join(result)

        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_path = os.path.join(output_folder, txt_filename)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ Saved: {txt_filename}")
