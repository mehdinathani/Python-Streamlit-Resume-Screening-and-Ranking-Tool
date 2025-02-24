# utils/text_extraction.py
import PyPDF2
import docx
import docx.document


def extract_text_from_pdf(pdf_path):
    """Extract Text from PDF file Object"""
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "
    return text.strip()


def extract_text_from_docx(docx_path):
    """Extracts text from Docx File."""
    doc = docx.document(docs_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return " ".join(full_text).strip()








    


