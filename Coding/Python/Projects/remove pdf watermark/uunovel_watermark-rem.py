
import fitz  # PyMuPDF
import cv2
import numpy as np
import io

def remove_watermark_red_channel(input_path, output_path):
    try:
        pdf_doc = fitz.open(input_path)
        output_docs = fitz.open()

        print(f"Processing: {input_path}")
        print("Using Red-Channel extraction for crystal clear text...")

        for page_num in range(len(pdf_doc)):
            page = pdf_doc.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            
            # 1. Image ko OpenCV format mein layein (RGB)
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.h, pix.w, 3))
            
            # 2. Sirf Red Channel ko alag karein (Index 0 for Red)
            # Scanned red watermark is mein white/gray ho jaye ga
            red_channel = img[:, :, 0]

            # 3. Contrast barhayein takay bacha-kucha watermark bilkul saaf ho jaye
            # Ye black text ko mazeed gehra (dark) kar dega
            _, clean_img = cv2.threshold(red_channel,180, 255, cv2.THRESH_BINARY)

            # 4. Save to PDF
            is_success, buffer = cv2.imencode(".png", clean_img)
            if is_success:
                img_bytes = buffer.tobytes()
                new_page = output_docs.new_page(width=page.rect.width, 
                                               height=page.rect.height)
                new_page.insert_image(new_page.rect, stream=img_bytes)
            
            print(f"Page {page_num + 1} cleaned.")

        output_docs.save(output_path)
        output_docs.close()
        pdf_doc.close()
        print(f"\nSuccess! New file saved: {output_path}")

    except Exception as e:
        print(f"\nError: {e}")

# Paths
input_file = r"C:\Users\PCS\Downloads\combined-1-5.pdf"
output_file = r"C:\Users\PCS\Downloads\combined_cleaned.pdf"

if __name__ == "__main__":
    remove_watermark_red_channel(input_file, output_file)









# import fitz  # PyMuPDF
# import cv2
# import numpy as np

# def clean_scanned_pdf(input_path, output_path):
#     try:
#         pdf_doc = fitz.open(input_path)
#         output_docs = fitz.open()

#         print(f"Processing: {input_path}")

#         for page_num in range(len(pdf_doc)):
#             page = pdf_doc.load_page(page_num)
            
#             # Resolution ko 3x kar rahe hain taake text ki quality barqarar rahe
#             pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
#             img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.h, pix.w, 3)).copy()
            
#             # HSV conversion
#             hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#             # 1. Color Masking (Pink aur Red ko target karna)
#             # Pink
#             lower_pink, upper_pink = np.array([140, 15, 15]), np.array([175, 255, 255])
#             # Red
#             lower_red1, upper_red1 = np.array([0, 30, 30]), np.array([10, 255, 255])
#             lower_red2, upper_red2 = np.array([170, 30, 30]), np.array([180, 255, 255])

#             mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)
#             mask_red = cv2.bitwise_or(cv2.inRange(hsv, lower_red1, upper_red1), 
#                                      cv2.inRange(hsv, lower_red2, upper_red2))
            
#             full_mask = cv2.bitwise_or(mask_pink, mask_red)

#             # Watermark wali jagah ko white kar dein
#             img[full_mask > 0] = [255, 255, 255]

#             # 2. Cleanup aur Text Restoration
#             gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            
#             # Median Blur: Ye chhote kaale dots (noise) ko khatam karega
#             cleaned = cv2.medianBlur(gray, 3)

#             # Adaptive Thresholding: Ye puray page par brightness ko adjust karke saaf B&W image dega
#             binary = cv2.adaptiveThreshold(cleaned, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#                                           cv2.THRESH_BINARY, 15, 12)

#             # Morphological Operations: Broken text ko jorne aur huroof ko thora wazay karne ke liye
#             kernel = np.ones((1, 1), np.uint8)
#             # Dilate thora sa text ko mota karega, phir erode usey wapas sahi shape dega
#             final_img = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

#             # Page ko save karein
#             is_success, buffer = cv2.imencode(".png", final_img)
#             if is_success:
#                 img_bytes = buffer.tobytes()
#                 new_page = output_docs.new_page(width=page.rect.width, height=page.rect.height)
#                 new_page.insert_image(new_page.rect, stream=img_bytes)
            
#             print(f"Page {page_num + 1} cleaned.")

#         output_docs.save(output_path)
#         output_docs.close()
#         pdf_doc.close()
#         print(f"\nSuccess! Cleaned PDF saved at:\n{output_path}")

#     except Exception as e:
#         print(f"\nError: {e}")

# # Paths
# input_file = r"C:\Users\PCS\Downloads\combined.pdf"
# output_file = r"C:\Users\PCS\Downloads\combined_cleaned.pdf"

# if __name__ == "__main__":
#     clean_scanned_pdf(input_file, output_file)