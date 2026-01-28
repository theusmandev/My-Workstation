import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PIL import Image


def image_to_pdf_page(image_path, output_path):
    """Convert a PNG image into a single-page PDF (A4 size)."""
    img = Image.open(image_path).convert("RGB")
    img_width, img_height = img.size

    c = canvas.Canvas(output_path, pagesize=A4)
    a4_width, a4_height = A4

    # Maintain aspect ratio
    ratio = min(a4_width / img_width, a4_height / img_height)
    new_width = img_width * ratio
    new_height = img_height * ratio
    x = (a4_width - new_width) / 2
    y = (a4_height - new_height) / 2

    c.drawImage(image_path, x, y, new_width, new_height)
    c.showPage()
    c.save()


def replace_first_page_with_image(pdf_path, image_path, output_path):
    """Replace the first page of a PDF with a PNG converted to PDF."""
    temp_pdf = "temp_page.pdf"
    image_to_pdf_page(image_path, temp_pdf)

    # ✅ Read temp image PDF completely before closing it
    img_reader = PdfReader(temp_pdf)
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Add new first page (from image)
    writer.add_page(img_reader.pages[0])

    # Add rest of the original pages
    for i in range(1, len(reader.pages)):
        writer.add_page(reader.pages[i])

    # Write output
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

    # Cleanup
    os.remove(temp_pdf)


def main():
    pdf_folder = r"E:\kiran complete\2006 - Copy"  # 📂 PDF folder path
    png_folder = r"E:\kiran complete\2006 - Copy\pngs\enhanced"  # 📂 PNG folder path

    output_folder = os.path.join(pdf_folder, "updated_pdfs")
    os.makedirs(output_folder, exist_ok=True)

    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf_name = os.path.splitext(pdf_file)[0]
        png_path = os.path.join(png_folder, pdf_name + ".png")
        pdf_path = os.path.join(pdf_folder, pdf_file)
        output_path = os.path.join(output_folder, pdf_file)

        if os.path.exists(png_path):
            print(f"✅ Replacing first page for: {pdf_file}")
            replace_first_page_with_image(pdf_path, png_path, output_path)
        else:
            print(f"⚠️ No matching PNG found for {pdf_file}, copying original...")
            with open(pdf_path, "rb") as src, open(output_path, "wb") as dst:
                dst.write(src.read())

    print("\n🎉 All PDFs processed successfully!")
    print(f"📁 Updated PDFs saved in: {output_folder}")


if __name__ == "__main__":
    main()
