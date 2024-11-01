import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, num_files):
    pdf = PdfReader(input_pdf)
    total_pages = len(pdf.pages)
    pages_per_file = total_pages // num_files
    remainder = total_pages % num_files

    for i in range(num_files):
        pdf_writer = PdfWriter()
        start_page = i * pages_per_file
        end_page = start_page + pages_per_file + (1 if i < remainder else 0)
        for page_num in range(start_page, end_page):
            pdf_writer.add_page(pdf.pages[page_num])
        output_filename = f"{os.path.splitext(os.path.basename(input_pdf))[0]}_{i+1}.pdf"
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print(f"Created: {output_filename}")

# Example usage
input_pdf = 'GPO-J6-REPORT.pdf'
num_files = 10  # Specify the number of smaller PDFs you want
split_pdf(input_pdf, num_files)