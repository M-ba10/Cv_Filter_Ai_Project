import re
import spacy

# Charger le modèle spaCy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):


    # Supprimer les espaces multiples
    text = re.sub(r"\s+", " ", text)

    # Supprimer les caractères spéciaux inutiles
    text = re.sub(r"[^\w\s@.+-]", " ", text)

    return text.strip()


def preprocess_text(text):


    cleaned_text = clean_text(text)

    doc = nlp(cleaned_text)

    tokens = []

    for token in doc:

        if (
            not token.is_stop
            and not token.is_punct
            and len(token.text) > 2
        ):

            tokens.append(token.lemma_.lower())

    return tokens