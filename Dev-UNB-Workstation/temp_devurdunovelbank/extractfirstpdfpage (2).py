import os
from PyPDF2 import PdfReader, PdfWriter

# Folder ka path jahan PDFs hain
folder_path = r"C:\Users\Latitude\Downloads\uns"

# Nayi PDF file jismein extract pages merge honge
output_pdf_path = r'D:\New folder\merged_first_pages.pdf'

# Naya PDF writer object
pdf_writer = PdfWriter()

# Folder ke saare files ko iterate karo
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Full file path
        file_path = os.path.join(folder_path, filename)

        # PDF reader object se PDF file ko read karo
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            
            # Agar PDF ke pages available hain to pehla page extract karo
            if pdf_reader.pages:
                first_page = pdf_reader.pages[0]
                
                # Pehla page writer mein add karo
                pdf_writer.add_page(first_page)

# Saare pages ko ek file mein save karo
with open(output_pdf_path, 'wb') as output_pdf_file:
    pdf_writer.write(output_pdf_file)

print(f'Successfully merged first pages into {output_pdf_path}')
