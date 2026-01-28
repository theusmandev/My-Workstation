import os
import fitz  # PyMuPDF

# PDF files ka folder
folder_path = r"C:\Users\PCS\Downloads\New folder (4)"

# Output folder jahan images save hongi
output_image_folder = r"C:\Users\PCS\Downloads\New folder (4)ok"
os.makedirs(output_image_folder, exist_ok=True)

# Har file ke liye processing
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        
        # PDF open karo
        doc = fitz.open(pdf_path)

        # Sirf first 2 pages extract karo (0-based indexing)
        for page_num in range(min(2, len(doc))):  # handle PDFs with less than 2 pages
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=150)  # DPI can be increased for higher quality
            
            # File name create karo based on PDF name and page number
            base_name = os.path.splitext(filename)[0]
            image_name = f"{base_name}_page{page_num+1}.png"
            image_path = os.path.join(output_image_folder, image_name)

            # Save image
            pix.save(image_path)

        doc.close()

print(f"Images successfully saved in: {output_image_folder}")
