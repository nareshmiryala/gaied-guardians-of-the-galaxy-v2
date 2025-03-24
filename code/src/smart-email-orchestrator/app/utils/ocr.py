from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    """
    Extracts text from an image using Optical Character Recognition (OCR).

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    str: The extracted text from the image.
    """
    try:
        # Open the image file
        img = Image.open(image_path)
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error occurred while processing the image: {e}")
        return ""