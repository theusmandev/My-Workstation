import os
from PyPDF2 import PdfReader, PdfWriter

# Input folder jahan PDFs majood hain
input_folder = r"C:\Users\Latitude\Downloads\uns"

# Output folder jahan modified PDFs save hongi
output_folder = "D:/New folder/output"

# Ensure output folder exists, warna create karein
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Saari PDF files ko list karein
pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

# Har PDF file ka pehla page remove karna
for pdf_file in pdf_files:
    pdf_path = os.path.join(input_folder, pdf_file)
    
    # PDF ko read karna
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Pehla page chor kar baqi pages ko nikalna
    for page_num in range(1, len(reader.pages)):
        writer.add_page(reader.pages[page_num])

    # Nai PDF file create karna jisme pehla page nahi hoga
    output_pdf_path = os.path.join(output_folder, f"modified_{pdf_file}")
    with open(output_pdf_path, 'wb') as output_pdf_file:
        writer.write(output_pdf_file)

print(f"Saari PDFs ka pehla page remove kar diya gaya hai aur modified files '{output_folder}' mein save kar di gayi hain!")
