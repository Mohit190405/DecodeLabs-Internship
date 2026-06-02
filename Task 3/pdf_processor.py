from pypdf import PdfReader

def extract_pdf_text(pdf_file):
    text = ""

    pdf = PdfReader(pdf_file)

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text