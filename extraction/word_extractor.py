import docx2txt

def extract_text_from_word(word_file):


    text = ""

    try:
        text = docx2txt.process(word_file)

    except Exception as e:
        print(f"Erreur Word : {e}")

    return text