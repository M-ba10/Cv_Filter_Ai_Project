import os

from extraction.pdf_extractor import extract_text_from_pdf
from extraction.word_extractor import extract_text_from_word
from extraction.image_ocr import extract_text_from_image

def extract_text(uploaded_file):


    filename = uploaded_file.name.lower()

    text = ""

    # PDF
    if filename.endswith(".pdf"):

        text = extract_text_from_pdf(uploaded_file)

    # WORD
    elif filename.endswith(".doc") or filename.endswith(".docx"):

        text = extract_text_from_word(uploaded_file)

    # IMAGE
    elif (
        filename.endswith(".jpg")
        or filename.endswith(".jpeg")
        or filename.endswith(".png")
    ):

        text = extract_text_from_image(uploaded_file)

    else:
        print("Format non supporté")

    return text