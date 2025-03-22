from pdfplumber import open as pdf_open
import pytesseract
from PIL import Image
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdf_open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text.strip()

def extract_text_from_file(file_path):
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        return extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file type: {}".format(file_path))