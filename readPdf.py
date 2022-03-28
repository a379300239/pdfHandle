import pdfplumber


def getPdfContent(filepath):
    contents = ''
    with pdfplumber.open(filepath) as pdf:
        pages = pdf.pages
        for page in pages:
            contents+=page.extract_text()
    return contents
