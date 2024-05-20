import PyPDF2

def pdf_to_text(pdf_path, text_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
        
    with open(text_path, 'w') as text_file:
        text_file.write(text)

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    text_path = input("Enter the path to save the text file: ")
    pdf_to_text(pdf_path, text_path)