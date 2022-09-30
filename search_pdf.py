from PyPDF4 import PdfFileReader
import os
import glob

def flatten_list(l):
    return [item for sublist in l for item in sublist]

def get_all_pdf_files():
    path = os.getcwd()
    pdf_files = []
    for folder, _, _ in os.walk(path):
        pdf_files.append(glob.glob(os.path.join(folder, "*.pdf")))
    return flatten_list(pdf_files)

def extract_pages_from_pdf_file(f):
    pdf = PdfFileReader(f)
    all_pages = []
    for page_number in range(pdf.getNumPages()):
        all_pages.append(pdf.getPage(page_number))
    return all_pages

def get_text_from_pdf(pdf_page):
    return pdf_page.extractText().strip().replace('\n','').lower()

def main():
    pdf_files = get_all_pdf_files()
    while True:
        input_string = input('What are you looking for: ').strip().lower()
        if input_string == 'end of work':
            break
        for pdf_file in pdf_files:
            file_name = pdf_file.split("\\")[-2:]
            f = open(pdf_file, 'rb')
            pdf_pages = extract_pages_from_pdf_file(f)
            for page_number in range(len(pdf_pages)):
                text = get_text_from_pdf(pdf_pages[page_number])
                if input_string in text:
                    print(f'File: {file_name}; page number: {page_number+1}')
            f.close()


if __name__ == "__main__":
    main()
