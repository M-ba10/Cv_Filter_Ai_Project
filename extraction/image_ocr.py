import pytesseract
from PIL import Image

def extract_text_from_image(image_file):


    text = ""

    try:

        image = Image.open(image_file)

        text = pytesseract.image_to_string(image, lang='fra')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    except Exception as e:
        print(f"Erreur OCR : {e}")

    return text