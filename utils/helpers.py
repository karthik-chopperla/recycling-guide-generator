# utils/helpers.py

import re

def clean_text(text: str) -> str:
    """
    Clean user input by lowering case and removing special characters.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()    # remove extra spaces
    return text
