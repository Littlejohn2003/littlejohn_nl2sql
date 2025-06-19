import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str):
    doc = nlp(text)
    return [(ent.label_, ent.text) for ent in doc.ents]
