# logic/confidence_estimator.py

def estimate_confidence(description: str, material_type: str) -> dict:
    """
    Simulates AI-style confidence scoring for material classification and guidance.
    Returns:
    - material_confidence: 0–100%
    - guidance_confidence: High / Moderate / Low
    - reason: What made this confidence level
    """
    desc = description.lower()

    keywords_map = {
        "Organic Waste": ["peel", "leftover", "rice", "vegetable", "curry", "food", "scrap"],
        "Plastic": ["plastic", "polybag", "bottle", "wrapper", "container", "pet"],
        "Paper": ["paper", "cardboard", "newspaper", "envelope", "magazine"],
        "Composite": ["foil", "tetra", "laminate", "chip bag", "multi-layer"],
        "E-Waste": ["charger", "cable", "battery", "phone", "device", "wire", "usb"],
        "Glass": ["glass", "bottle", "jar", "mirror", "broken"],
        "Metal": ["can", "tin", "aluminum", "steel", "foil", "metal"],
        "Textile": ["cloth", "fabric", "towel", "jeans", "shirt", "bedsheet"],
        "Hazardous Waste": ["paint", "chemical", "pesticide", "medicine", "cleaner"]
    }

    matched_keywords = keywords_map.get(material_type.replace("Contaminated ", ""), [])
    hits = sum(1 for word in matched_keywords if word in desc)

    # Confidence scoring rules
    if hits >= 3:
        score = 0.95
        guidance = "High"
        reason = f"Multiple strong keyword matches for {material_type.lower()}."
    elif hits == 2:
        score = 0.80
        guidance = "Moderate"
        reason = f"Moderate confidence based on partial keyword match."
    elif hits == 1:
        score = 0.60
        guidance = "Low"
        reason = f"Only one relevant keyword detected. May be ambiguous."
    else:
        score = 0.40
        guidance = "Low"
        reason = f"No reliable keywords matched. Classification is uncertain."

    return {
        "material_confidence": round(score * 100, 2),
        "guidance_confidence": guidance,
        "reason": reason
    }
