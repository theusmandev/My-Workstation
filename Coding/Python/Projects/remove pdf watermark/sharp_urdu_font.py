

import fitz  # PyMuPDF
import cv2
import numpy as np
import os
import img2pdf

def enhance_urdu_final_v2(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    temp_images = []

    print(f"Applying Advanced Morphological Filtering to {len(doc)} pages...")

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # Use 300 DPI for a balance between speed and quality
        pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
        
        img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
        img = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 1. Light Blur to merge 'hollow' edges into a solid form
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)

        # 2. Adaptive Thresholding (Strong C value to keep it thin)
        # 25 is the block size, 10 is the constant subtracted from the mean
        thresh = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 25, 10
        )

        # 3. Morphological Closing (Fills tiny holes inside letters)
        kernel_close = np.ones((2,2), np.uint8)
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_close)

        # 4. Final Thinning (Erosion)
        # This is the "secret sauce" to prevent bloating. 
        # On a white background, dilating the white space "shrinks" the black text.
        kernel_thin = np.ones((2,2), np.uint8)
        final_img = cv2.dilate(closed, kernel_thin, iterations=1)

        temp_name = f"page_v2_{page_num}.png"
        cv2.imwrite(temp_name, final_img)
        temp_images.append(temp_name)
        print(f"Page {page_num + 1} finalized.")

    print("Building crisp PDF...")
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(temp_images))

    # Cleanup
    for img_file in temp_images:
        os.remove(img_file)
    doc.close()
    
    print(f"\nSuccess! Your optimized novel is at:\n{output_pdf}")

# --- RUN ---
INPUT = r"C:\Users\PCS\Downloads\1v - Copy.pdf"
OUTPUT = r"C:\Users\PCS\Downloads\1v - Copy_CRISP_V2.pdf"

enhance_urdu_final_v2(INPUT, OUTPUT)







# import fitz  # PyMuPDF
# import cv2
# import numpy as np
# import os
# import img2pdf

# def enhance_urdu_final(input_pdf, output_pdf):
#     doc = fitz.open(input_pdf)
#     temp_images = []

#     print(f"Processing {len(doc)} pages with refined clarity...")

#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         # 300-400 DPI is the sweet spot for Urdu Nastaliq
#         pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
        
#         img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
#         img = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # 1. Light Sharpening 
#         # Using a center weight of 5 instead of 9 to prevent the 'bloated' look
#         kernel = np.array([[ 0, -1,  0],
#                            [-1,  5, -1],
#                            [ 0, -1,  0]])
#         sharpened = cv2.filter2D(gray, -1, kernel)

#         # 2. Adaptive Thresholding
#         # This prevents 'hollow' letters and handles uneven lighting/paper color
#         thresh = cv2.adaptiveThreshold(
#             sharpened, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#             cv2.THRESH_BINARY, 21, 15
#         )

#         # 3. Denoising
#         # Removes tiny black speckles from the background
#         denoised = cv2.medianBlur(thresh, 3)

#         # 4. Thinning (Erosion)
#         # If the text still feels too bold/bloated, this 'shaves' 1 pixel off the edges
#         # We use a 2x2 kernel for a very subtle thinning effect
#         kernel_thin = np.ones((2,2), np.uint8)
#         # Note: On a white background, cv2.dilate actually thins the BLACK text
#         final_img = cv2.dilate(denoised, kernel_thin, iterations=1)

#         temp_name = f"page_{page_num}.png"
#         cv2.imwrite(temp_name, final_img)
#         temp_images.append(temp_name)
#         print(f"Done: Page {page_num + 1}")

#     print("Finalizing PDF...")
#     with open(output_pdf, "wb") as f:
#         f.write(img2pdf.convert(temp_images))

#     # Cleanup
#     for img_file in temp_images:
#         os.remove(img_file)
#     doc.close()
    
#     print(f"\nSaved refined version to: {output_pdf}")

# # --- EXECUTION ---
# INPUT_FILE = r"C:\Users\PCS\Downloads\1v - Copy.pdf"
# OUTPUT_FILE = r"C:\Users\PCS\Downloads\1v - Copy_CRISP.pdf"

# enhance_urdu_final(INPUT_FILE, OUTPUT_FILE)

# import fitz  # PyMuPDF
# import cv2
# import numpy as np
# import os
# import img2pdf

# def enhance_urdu_refined(input_pdf, output_pdf):
#     doc = fitz.open(input_pdf)
#     temp_images = []

#     print(f"Refining {len(doc)} pages for better clarity...")

#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         # Increase DPI to 400 for better Urdu ligature detail
#         pix = page.get_pixmap(matrix=fitz.Matrix(400/72, 400/72))
        
#         img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
#         img = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # 1. Subtle Sharpening (Reduced the center weight from 9 to 7 to prevent bloating)
#         # This keeps the lines crisp without making them too thick
#         kernel = np.array([[ 0, -1,  0],
#                            [-1,  5, -1],
#                            [ 0, -1,  0]])
#         sharpened = cv2.filter2D(gray, -1, kernel)

#         # 2. Adaptive Thresholding
#         # This is better than Otsu for scanned novels because it handles 
#         # local variations in paper color/ink density.
#         final_img = cv2.adaptiveThreshold(
#             sharpened, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#             cv2.THRESH_BINARY, 15, 8
#         )

#         # 3. Optional: Median Blur to remove tiny speckles/noise
#         final_img = cv2.medianBlur(final_img, 3)

#         temp_name = f"refined_p{page_num}.png"
#         cv2.imwrite(temp_name, final_img)
#         temp_images.append(temp_name)
#         print(f"Processed page {page_num + 1}")

#     print("Reassembling PDF...")
#     with open(output_pdf, "wb") as f:
#         f.write(img2pdf.convert(temp_images))

#     # Cleanup
#     for img_file in temp_images:
#         os.remove(img_file)
#     doc.close()
    
#     print(f"\nDone! Optimized PDF saved at: {output_pdf}")

# # --- EXECUTION ---
# INPUT_FILE = r"C:\Users\PCS\Downloads\1v - Copy.pdf"
# OUTPUT_FILE = r"C:\Users\PCS\Downloads\1v - Copy_SHARP.pdf"

# enhance_urdu_refined(INPUT_FILE, OUTPUT_FILE)










# import fitz  # PyMuPDF
# import cv2
# import numpy as np
# import os
# import img2pdf

# def enhance_urdu_text(input_pdf, output_pdf):
#     # 1. Open the PDF
#     doc = fitz.open(input_pdf)
#     temp_images = []

#     print(f"Processing {len(doc)} pages...")

#     for page_num in range(len(doc)):
#         # 2. Convert PDF page to a high-res image (DPI 300)
#         page = doc.load_page(page_num)
#         pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
        
#         # Convert Pixmap to OpenCV format
#         img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
#         img = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)

#         # 3. Increase Contrast & "Saturation" (Intensity of Ink)
#         # We convert to grayscale first
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
#         # CLAHE helps bring out faded text without making the background dark
#         clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
#         contrast_img = clahe.apply(gray)

#         # 4. Sharpening the edges of Nastaliq script
#         kernel = np.array([[-1,-1,-1], 
#                            [-1, 9,-1],
#                            [-1,-1,-1]])
#         sharpened = cv2.filter2D(contrast_img, -1, kernel)

#         # 5. Thresholding (Clean white background, pure black text)
#         _, final_img = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#         # Save temporary page image
#         temp_name = f"page_{page_num}.png"
#         cv2.imwrite(temp_name, final_img)
#         temp_images.append(temp_name)
#         print(f"Processed page {page_num + 1}")

#     # 6. Merge images back into a high-quality PDF
#     print("Saving final PDF...")
#     with open(output_pdf, "wb") as f:
#         f.write(img2pdf.convert(temp_images))

#     # Cleanup
#     for img_file in temp_images:
#         os.remove(img_file)
#     doc.close()
    
#     print(f"\nSuccess! Enhanced PDF saved at: {output_pdf}")

# # --- EXECUTION ---
# INPUT_FILE = r"C:\Users\PCS\Downloads\1v - Copy.pdf"
# OUTPUT_FILE = r"C:\Users\PCS\Downloads\1v - Copy_ENHANCED.pdf"

# enhance_urdu_text(INPUT_FILE, OUTPUT_FILE)