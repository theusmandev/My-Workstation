# import fitz  # PyMuPDF
# from PIL import Image
# import io
# import os

# def compress_pdf(input_pdf, output_pdf, max_size_mb):
#     max_size_bytes = max_size_mb * 1024 * 1024

#     # PDF فائل کو کھولیں
#     doc = fitz.open(input_pdf)

#     # ہر صفحے پر جائیں اور تصاویر کو کمپریس کریں
#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         image_list = page.get_images(full=True)

#         for img_index, img in enumerate(image_list):
#             xref = img[0]
#             base_image = doc.extract_image(xref)
#             image_bytes = base_image["image"]
#             image = Image.open(io.BytesIO(image_bytes))

#             # تصویر کو کمپریس کریں
#             image = image.convert("RGB")
#             image.save("temp_image.jpg", quality=85)
#             compressed_image = Image.open("temp_image.jpg")
#             image_bytes = io.BytesIO()
#             compressed_image.save(image_bytes, format="JPEG", quality=85)
#             image_bytes = image_bytes.getvalue()

#             # کمپریس شدہ تصویر کو PDF میں ڈالیں
#             doc.update_image(xref, image=image_bytes)

#     # PDF فائل کو محفوظ کریں
#     doc.save(output_pdf)
#     doc.close()

#     # اگر فائل کا سائز اب بھی زیادہ ہے تو دوبارہ کمپریس کریں
#     while os.path.getsize(output_pdf) > max_size_bytes:
#         compress_pdf(output_pdf, output_pdf, max_size_mb)

# # استعمال کی مثال
# input_pdf = r"C:\Users\Latitude\Downloads\pdf24_merged.pdf"
# output_pdf = r"C:\Users\Latitude\Downloads\pdf24_merged11.pdf"
# max_size_mb = 50

# compress_pdf(input_pdf, output_pdf, max_size_mb)









# import fitz  # PyMuPDF
# import os

# def compress_text_pdf(input_pdf, output_pdf, max_size_mb):
#     max_size_bytes = max_size_mb * 1024 * 1024

#     # PDF فائل کو کھولیں
#     doc = fitz.open(input_pdf)

#     # غیر ضروری میٹا ڈیٹا کو ہٹائیں
#     doc.set_metadata({})  # میٹا ڈیٹا کو خالی کر دیں

#     # فونٹس کو کم کریں اور دیگر غیر ضروری ڈیٹا کو ہٹائیں
#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         page.clean_contents()  # غیر ضروری مواد کو صاف کریں

#     # PDF فائل کو محفوظ کریں
#     doc.save(output_pdf, garbage=50, deflate=True)  # فائل کو کمپریس کریں
#     doc.close()

#     # فائل کا سائز چیک کریں
#     if os.path.getsize(output_pdf) > max_size_bytes:
#         print("فائل کا سائز اب بھی زیادہ ہے۔ مزید کمپریشن ممکن نہیں ہے۔")
#     else:
#         print(f"فائل کا سائز کم ہو کر {os.path.getsize(output_pdf) / 1024 / 1024:.2f} MB ہو گیا ہے۔")

# # استعمال کی مثال
# input_pdf = r"C:\Users\Latitude\Downloads\pdf24_merged.pdf"
# output_pdf = r"C:\Users\Latitude\Downloads\pdf24_merged11.pdf"
# max_size_mb = 50  # مطلوبہ زیادہ سے زیادہ سائز (MB میں)

# compress_text_pdf(input_pdf, output_pdf, max_size_mb)












import os
import subprocess

input_folder = r"C:\Users\Latitude\Downloads\New folder"
output_folder = r"C:\Users\Latitude\Downloads\New folder (2)"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for item in os.listdir(input_folder):
    if item.endswith('.pdf'):
        input_path = os.path.join(input_folder, item)
        output_path = os.path.join(output_folder, item)
        subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                        '-dPDFSETTINGS=/screen', '-dNOPAUSE', '-dQUIET', '-dBATCH',
                        '-sOutputFile=' + output_path, input_path])