





import fitz  # PyMuPDF
from PIL import Image
import io

def remove_red_watermark(input_pdf, output_pdf):
    # Open the PDF
    pdf_doc = fitz.open(input_pdf)
    output_docs = fitz.open()

    for page_num in range(len(pdf_doc)):
        # 1. Convert PDF page to high-resolution image
        page = pdf_doc.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) # Increase multiplier for better quality
        
        # 2. Open with PIL
        img = Image.open(io.BytesIO(pix.tobytes()))
        img = img.convert("RGB")
        datas = img.getdata()

        new_data = []
        for item in datas:
            # item[0] is Red, item[1] is Green, item[2] is Blue
            # Logic: If the pixel is "Reddish" (High Red, Lower Green/Blue), make it white
            if item[0] > 150 and item[1] < 150 and item[2] < 150:
                new_data.append((255, 255, 255))  # Turn to White
            else:
                new_data.append(item)

        img.putdata(new_data)

        # 3. Convert back to PDF page
        pdf_bytes = io.BytesIO()
        img.save(pdf_bytes, format="PDF")
        
        # Add this cleaned page to our new PDF
        cleaned_page_doc = fitz.open("pdf", pdf_bytes.getvalue())
        output_docs.insert_pdf(cleaned_page_doc)

    # Save the final result
    output_docs.save(output_pdf)
    output_docs.close()
    pdf_doc.close()
    print(f"Success! Cleaned PDF saved as: {output_pdf}")

# Usage
remove_red_watermark(r"C:\Users\PCS\Downloads\Ibtihal epi_1.pdf", r"C:\Users\PCS\Downloads\Ibtihal epi_1ok.pdf")