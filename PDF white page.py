import PyPDF2
import os

def add_pages_to_pdf(pdf_path, num_pages):
    # Check if the PDF file path exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        return

    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Create a new PDF writer for each combination of pages
        for i in range(1, num_pages + 1):
            writer = PyPDF2.PdfWriter()

            # Add existing pages to the new PDF writer
            for page in reader.pages:
                writer.add_page(page)

            # Add additional blank pages
            for _ in range(i):
                new_page = PyPDF2.PageObject.create_blank_page(None, 612, 792)  # Standard US Letter size
                writer.add_page(new_page)

            # Create a new PDF file with the added pages
            new_pdf_name = f'a{i}.pdf'
            new_pdf_path = os.path.join(os.path.dirname(pdf_path), new_pdf_name)
            with open(new_pdf_path, 'wb') as new_file:
                writer.write(new_file)

            print(f"New PDF '{new_pdf_name}' with {i} additional pages has been created.")

# Path to the PDF file
pdf_path = 'C:/Users/iagol/Downloads/a.pdf'

# Specify the maximum number of pages
max_pages = 5

# Call the function to add the pages and save the new PDFs
add_pages_to_pdf(pdf_path, max_pages)