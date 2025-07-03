"""
Reject abstract or non-object inputs.
"""

def is_non_recyclable_input(text: str) -> bool:
    """
    Returns True if the input is likely an abstract, vague, or non-object word.
    Examples: "beautiful", "education", "freedom", "G Telugu", "AI for education"
    """
    abstract_keywords = [
        "beautiful", "education", "love", "hope", "happiness",
        "freedom", "AI for education", "god", "dream", "goal",
        "motivation", "spirit", "energy", "music", "light", "faith"
    ]
    text_lower = text.lower().strip()
    # If input is only one word or matches any known abstract concepts
    return len(text_lower.split()) == 1 or any(word in text_lower for word in abstract_keywords)
