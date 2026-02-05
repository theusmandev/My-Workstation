import os
import fitz  # PyMuPDF

def pdfs_first_page_to_pngs(folder_path):
    # Get Downloads folder path
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Agar output folder nahi hai to bana do
    os.makedirs(downloads_folder, exist_ok=True)

    # Folder ke andar jitni bhi files hain unpar loop
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)

            try:
                # Extract PDF file name (without extension)
                pdf_name = os.path.splitext(filename)[0]

                # Output image path (same name as PDF)
                output_name = f"{pdf_name}.png"
                output_path = os.path.join(downloads_folder, output_name)

                # Open PDF and extract first page
                doc = fitz.open(pdf_path)
                if doc.page_count > 0:
                    page = doc[0]  # first page
                    pix = page.get_pixmap()
                    pix.save(output_path)
                    print(f"✅ First page of '{filename}' saved as '{output_path}'")
                else:
                    print(f"⚠️ '{filename}' has no pages.")

            except Exception as e:
                print(f"❌ Error processing '{filename}': {e}")


# Example usage
pdf_folder = r"C:\Users\PCS\Downloads\quratulainhaider\extract" # apne PDFs ka folder path yahan do
pdfs_first_page_to_pngs(pdf_folder)
