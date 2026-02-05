import os
from PyPDF2 import PdfReader, PdfWriter

def remove_page_from_pdf(input_pdf, output_pdf, page_to_remove):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i in range(len(reader.pages)):
        if i != (page_to_remove - 1):  # page_to_remove 1-based hai
            writer.add_page(reader.pages[i])

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"✅ Page {page_to_remove} removed. Output saved at: {output_pdf}")


if __name__ == "__main__":
    # Yahan apna input PDF ka path dein
    input_pdf = r"C:\Users\PCS\Downloads\Hashim Nadeem Novels\replace\Aik Mohabbat Aur Sahi.pdf"
    # Output file ka naam
    output_pdf = r"C:\Users\PCS\Downloads\Hashim Nadeem Novels\replace\Aik Mohabbat Aur Sahiok.pdf"
    # Kaunsa page remove karna hai (1-based)
    page_to_remove = 2

    remove_page_from_pdf(input_pdf, output_pdf, page_to_remove)
