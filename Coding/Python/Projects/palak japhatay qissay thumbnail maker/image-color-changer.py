



# #v2


# import fitz  # PyMuPDF 
# import cv2
# import numpy as np

# def process_and_upscale_pdf(input_pdf, output_pdf, hex_color="#FFEFD5", upscale_factor=3):
#     """
#     upscale_factor: 2 is good, 3 is high quality, 4 is ultra high (but slow).
#     """
#     # 1. Convert hex to BGR
#     hex_color = hex_color.lstrip('#')
#     rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
#     target_bgr = np.array([rgb[2], rgb[1], rgb[0]], dtype=np.float32)

#     doc = fitz.open(input_pdf)
#     new_doc = fitz.open()

#     # Define zoom matrix for upscaling (upscale_factor x upscale_factor)
#     # This increases the resolution of the image extraction
#     matrix = fitz.Matrix(upscale_factor, upscale_factor)

#     print(f"Processing {len(doc)} pages with {upscale_factor}x upscaling...")

#     for page_index in range(len(doc)):
#         page = doc.load_page(page_index)
        
#         # 2. Get high-resolution pixmap (Upscaling happens here)
#         pix = page.get_pixmap(matrix=matrix, colorspace=fitz.csRGB)
        
#         # Convert pixmap to numpy array
#         img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, 3)
        
#         # 3. Apply color transformation
#         img_float = img.astype(np.float32) / 255.0
#         result = (img_float * target_bgr).astype(np.uint8)

#         # 4. Encode with high quality (JPEG quality 95+)
#         # Using '.png' would be lossless but makes the PDF file size very large.
#         _, img_encoded = cv2.imencode(".jpg", result, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
#         img_bytes = img_encoded.tobytes()

#         # 5. Insert into new PDF
#         # Note: We keep the original page dimensions so it prints correctly, 
#         # but the image inside has higher pixel density.
#         new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
#         new_page.insert_image(page.rect, stream=img_bytes)
        
#         print(f"Page {page_index + 1} processed.")

#     # 6. Save with optimization
#     new_doc.save(output_pdf, garbage=4, deflate=True)
#     new_doc.close()
#     doc.close()
#     print(f"\nFinished! High-quality PDF saved to: {output_pdf}")

# # --- SETTINGS ---
# input_path = r"C:\Users\PCS\Downloads\Ibtihal epi_1\1v.pdf"
# output_path = r"C:\Users\PCS\Downloads\1v_high_res.pdf"

# # Call the function (upscale_factor=3 is usually the "sweet spot" for books)
# process_and_upscale_pdf(input_path, output_path, "#FFEFD5", upscale_factor=3)










#v1

# import fitz  # PyMuPDF
# import cv2
# import numpy as np

# def process_scanned_pdf(input_pdf, output_pdf, hex_color="#FFEFD5"):
#     # 1. Convert hex to BGR for OpenCV
#     hex_color = hex_color.lstrip('#')
#     rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
#     target_bgr = np.array([rgb[2], rgb[1], rgb[0]], dtype=np.float32)

#     # 2. Open source and create target PDF
#     doc = fitz.open(input_pdf)
#     new_doc = fitz.open()

#     print(f"Processing {len(doc)} pages...")

#     for page_index in range(len(doc)):
#         page = doc.load_page(page_index)
        
#         # Get image of the page
#         pix = page.get_pixmap()
        
#         # Convert pixmap to numpy array (Handling RGB)
#         img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, 3)
        
#         # 3. Apply the color transformation
#         img_float = img.astype(np.float32) / 255.0
#         result = (img_float * target_bgr).astype(np.uint8)

#         # 4. Encode image to memory
#         _, img_encoded = cv2.imencode(".jpg", result)
#         img_bytes = img_encoded.tobytes()

#         # 5. Create new page and insert the colored image
#         # We use page.rect to ensure the new page is the same size as the old one
#         new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
#         new_page.insert_image(page.rect, stream=img_bytes)
        
#         print(f"Page {page_index + 1} done.")

#     # 6. Save the final PDF
#     new_doc.save(output_pdf)
#     new_doc.close()
#     doc.close()
#     print(f"\nSuccess! Saved to: {output_pdf}")

# # --- EXECUTION ---
# # Note: Use 'r' before paths to handle backslashes correctly in Windows
# input_path = r"C:\Users\PCS\Downloads\Ibtihal epi_1\1v.pdf"
# output_path = r"C:\Users\PCS\Downloads\Ibtihal epi_1\1vokk.pdf"

# process_scanned_pdf(input_path, output_path, "#FFEFD5")



#image color changed

import cv2
import numpy as np

def change_image_background(input_path, output_path, hex_color="#FFEFD5"):
    # 1. Convert hex color to BGR (OpenCV uses BGR format)
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    target_color_bgr = np.array([rgb[2], rgb[1], rgb[0]], dtype=np.float32)

    # 2. Load the image
    img = cv2.imread(input_path)
    if img is None:
        print("Error: Could not load image.")
        return

    # 3. Process the image
    # We treat the image as a mask. 
    # White areas (255) will become the target color.
    # Black areas (0) will remain black.
    # This formula handles anti-aliasing (gray edges) smoothly.
    img_float = img.astype(np.float32) / 255.0
    result = img_float * target_color_bgr

    # 4. Convert back to standard image format (uint8)
    result = np.clip(result, 0, 255).astype(np.uint8)

    # 5. Save the result
    cv2.imwrite(output_path, result)
    print(f"Successfully saved to: {output_path}")

# Usage
change_image_background(r"C:\Users\PCS\Downloads\Bano .png", r"C:\Users\PCS\Downloads\Gemini_Generated_Image_2qknvy2qkn000vy2qkn.png", '#FFEFD5')