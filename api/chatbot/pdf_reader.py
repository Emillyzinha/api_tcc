import PyPDF2

def read_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    idx = pdf_reader.pages
    for i in range(len(idx)):
        print(pdf_reader.pages[i].extract_text())


if __name__ == "__main__":
    teste = []