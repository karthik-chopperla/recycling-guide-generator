# logic/material_classifier.py

def classify_material(description: str) -> tuple[str, float, str]:
    """
    Classifies the material type of a given item description using dynamic logic rules.
    Returns: (material_type, confidence_score, explanation)
    """
    desc = description.lower()
    confidence = 0.0
    explanation = ""

    # Organic Waste
    if any(word in desc for word in ["peel", "leftover", "curry", "vegetable", "food", "fruit", "rice"]):
        return "Organic Waste", 0.95, "Detected food-related terms commonly linked to organic waste."

    # Plastic
    if any(word in desc for word in ["plastic", "pet", "polybag", "wrapper", "bottle"]):
        return "Plastic", 0.9, "Detected plastic-related terms."

    # Paper
    if any(word in desc for word in ["cardboard", "newspaper", "paper", "magazine", "box"]):
        return "Paper", 0.9, "Detected paper-related terms."

    # Glass
    if any(word in desc for word in ["glass", "jar", "bottle", "mirror"]):
        return "Glass", 0.9, "Detected glass-related terms."

    # Metal
    if any(word in desc for word in ["can", "foil", "metal", "aluminum", "tin"]):
        return "Metal", 0.85, "Detected metallic terms."

    # Composite (multi-material)
    if any(word in desc for word in ["foil-lined", "tetra pak", "chip packet", "multi-layer"]):
        return "Composite", 0.88, "Detected multi-material item, classified as composite."

    # E-Waste
    if any(word in desc for word in ["charger", "usb", "battery", "phone", "device"]):
        return "E-Waste", 0.92, "Detected electronic item, classified as e-waste."

    # Hazardous
    if any(word in desc for word in ["paint", "chemical", "pesticide", "medicine"]):
        return "Hazardous Waste", 0.93, "Detected toxic/hazardous item keywords."

    # Textile
    if any(word in desc for word in ["cloth", "fabric", "jeans", "towel", "shirt", "bed"]):
        return "Textile", 0.9, "Detected fabric-related terms."

    # If no strong match found
    return "Uncertain", 0.3, "No strong material-related terms found. Please provide more detail."
