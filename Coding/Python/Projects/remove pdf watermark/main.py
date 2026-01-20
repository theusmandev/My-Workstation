


#v3


# import fitz  # PyMuPDF
# import cv2
# import numpy as np
# import io

# def professional_clean_pdf(input_path, output_path):
#     try:
#         pdf_doc = fitz.open(input_path)
#         output_docs = fitz.open()

#         print(f"Cleaning: {input_path}")

#         for page_num in range(len(pdf_doc)):
#             page = pdf_doc.load_page(page_num)
#             pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            
#             # 1. Image ko RGB mein convert karein
#             img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.h, pix.w, 3))
            
#             # 2. Sirf Red Channel lein (Yahan watermark white ho jata hai)
#             red_channel = img[:, :, 0]

#             # 3. BACKGROUND NORMALIZATION (The Magic Step)
#             # Paper ke grey rang ko khatam karke pure white karne ke liye
#             dilated_img = cv2.dilate(red_channel, np.ones((7,7), np.uint8))
#             bg_img = cv2.medianBlur(dilated_img, 21)
#             diff_img = 255 - cv2.absdiff(red_channel, bg_img)
#             norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)

#             # 4. FINAL CLEANUP
#             # Jo cheez 230 se zyada light hai usay pure white (255) kar do
#             _, final_img = cv2.threshold(norm_img, 230, 255, cv2.THRESH_BINARY)

#             # 5. Save to PDF
#             is_success, buffer = cv2.imencode(".png", final_img)
#             if is_success:
#                 img_bytes = buffer.tobytes()
#                 new_page = output_docs.new_page(width=page.rect.width, height=page.rect.height)
#                 new_page.insert_image(new_page.rect, stream=img_bytes)
            
#             print(f"Page {page_num + 1} processed.")

#         output_docs.save(output_path)
#         output_docs.close()
#         pdf_doc.close()
#         print(f"\nSuccess! Mubarak ho, result check karein:\n{output_path}")

#     except Exception as e:
#         print(f"\nError: {e}")

# # Paths
# input_file = r"C:\Users\PCS\Downloads\Ibtihal epi_1.pdf"
# output_file = r"C:\Users\PCS\Downloads\Ibtihal epi_1ok.pdf"

# if __name__ == "__main__":
#     professional_clean_pdf(input_file, output_file)






#good with bold text color good excellent   v2


# import fitz  # PyMuPDF
# import cv2
# import numpy as np
# import io

# def remove_watermark_red_channel(input_path, output_path):
#     try:
#         pdf_doc = fitz.open(input_path)
#         output_docs = fitz.open()

#         print(f"Processing: {input_path}")
#         print("Using Red-Channel extraction for crystal clear text...")

#         for page_num in range(len(pdf_doc)):
#             page = pdf_doc.load_page(page_num)
#             pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            
#             # 1. Image ko OpenCV format mein layein (RGB)
#             img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.h, pix.w, 3))
            
#             # 2. Sirf Red Channel ko alag karein (Index 0 for Red)
#             # Scanned red watermark is mein white/gray ho jaye ga
#             red_channel = img[:, :, 0]

#             # 3. Contrast barhayein takay bacha-kucha watermark bilkul saaf ho jaye
#             # Ye black text ko mazeed gehra (dark) kar dega
#             _, clean_img = cv2.threshold(red_channel, 200, 255, cv2.THRESH_BINARY)

#             # 4. Save to PDF
#             is_success, buffer = cv2.imencode(".png", clean_img)
#             if is_success:
#                 img_bytes = buffer.tobytes()
#                 new_page = output_docs.new_page(width=page.rect.width, 
#                                                height=page.rect.height)
#                 new_page.insert_image(new_page.rect, stream=img_bytes)
            
#             print(f"Page {page_num + 1} cleaned.")

#         output_docs.save(output_path)
#         output_docs.close()
#         pdf_doc.close()
#         print(f"\nSuccess! New file saved: {output_path}")

#     except Exception as e:
#         print(f"\nError: {e}")

# # Paths
# input_file = r"C:\Users\PCS\Downloads\Ibtihal epi_1.pdf"
# output_file = r"C:\Users\PCS\Downloads\Ibtihal epi_1ok.pdf"

# if __name__ == "__main__":
#     remove_watermark_red_channel(input_file, output_file)






#use this good best        v1

# import fitz  # PyMuPDF
# import cv2
# import numpy as np
# import io

# def clean_scanned_pdf(input_path, output_path):
#     try:
#         # 1. Original PDF open karein
#         pdf_doc = fitz.open(input_path)
#         # 2. Aik khali PDF document banayein
#         output_docs = fitz.open()

#         print(f"Processing: {input_path}")
#         print("Please wait, cleaning pages...")

#         for page_num in range(len(pdf_doc)):
#             # Page load karein
#             page = pdf_doc.load_page(page_num)
            
#             # Page ko image mein badlein (Resolution 2x rakhi hai clarity ke liye)
#             pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            
#             # Image data ko OpenCV format mein layein
#             img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.h, pix.w, 3))
            
#             # Grayscale (B&W) mein badlein
#             gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            
#             # Thresholding: 150 se halkay colors ko white kar do (Watermark removal)
#             _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

#             # Clean image ko PNG format mein convert karein
#             is_success, buffer = cv2.imencode(".png", thresh)
#             if is_success:
#                 img_bytes = buffer.tobytes()
                
#                 # Naye PDF mein page add karein (Original size ke mutabiq)
#                 # pix.w aur pix.h ko Matrix(2,2) ki wajah se adjust karna hoga
#                 new_page = output_docs.new_page(width=page.rect.width, 
#                                                height=page.rect.height)
                
#                 # Saaf shuda image ko page par lagayein
#                 new_page.insert_image(new_page.rect, stream=img_bytes)
            
#             print(f"Done: Page {page_num + 1}")

#         # Final file save karein
#         output_docs.save(output_path)
#         output_docs.close()
#         pdf_doc.close()
#         print(f"\nSuccess! Cleaned PDF saved at:\n{output_path}")

#     except Exception as e:
#         print(f"\nAn error occurred: {e}")

# # Aapke Paths
# input_file = r"C:\Users\PCS\Downloads\Ibtihal epi_1.pdf"
# output_file = r"C:\Users\PCS\Downloads\Ibtihal epi_1ok.pdf"

# if __name__ == "__main__":
#     clean_scanned_pdf(input_file, output_file)








# import fitz  # PyMuPDF
# from PIL import Image
# import io

# def remove_red_watermark(input_pdf, output_pdf):
#     # Open the PDF
#     pdf_doc = fitz.open(input_pdf)
#     output_docs = fitz.open()

#     for page_num in range(len(pdf_doc)):
#         # 1. Convert PDF page to high-resolution image
#         page = pdf_doc.load_page(page_num)
#         pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) # Increase multiplier for better quality
        
#         # 2. Open with PIL
#         img = Image.open(io.BytesIO(pix.tobytes()))
#         img = img.convert("RGB")
#         datas = img.getdata()

#         new_data = []
#         for item in datas:
#             # item[0] is Red, item[1] is Green, item[2] is Blue
#             # Logic: If the pixel is "Reddish" (High Red, Lower Green/Blue), make it white
#             if item[0] > 150 and item[1] < 150 and item[2] < 150:
#                 new_data.append((255, 255, 255))  # Turn to White
#             else:
#                 new_data.append(item)

#         img.putdata(new_data)

#         # 3. Convert back to PDF page
#         pdf_bytes = io.BytesIO()
#         img.save(pdf_bytes, format="PDF")
        
#         # Add this cleaned page to our new PDF
#         cleaned_page_doc = fitz.open("pdf", pdf_bytes.getvalue())
#         output_docs.insert_pdf(cleaned_page_doc)

#     # Save the final result
#     output_docs.save(output_pdf)
#     output_docs.close()
#     pdf_doc.close()
#     print(f"Success! Cleaned PDF saved as: {output_pdf}")

# # Usage
# remove_red_watermark(r"C:\Users\PCS\Downloads\Ibtihal epi_1.pdf", r"C:\Users\PCS\Downloads\Ibtihal epi_1ok.pdf")