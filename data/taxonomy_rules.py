# data/taxonomy_rules.py

def get_taxonomy_keywords():
    """
    Returns a simulated taxonomy dictionary of keywords mapped to material types.
    This mimics a real-world materials ontology used by recycling facilities.
    """
    return {
        "Plastic": ["plastic", "bottle", "poly", "wrap", "container", "bag", "film"],
        "Glass": ["glass", "jar", "bottle", "mirror", "bulb"],
        "Paper": ["paper", "newspaper", "cardboard", "magazine", "book"],
        "Metal": ["metal", "can", "foil", "tin", "aluminum", "steel"],
        "E-Waste": ["battery", "laptop", "mobile", "charger", "phone", "wire"],
        "Organic": ["food", "vegetable", "fruit", "peel", "waste", "compost"],
        "Hazardous": ["paint", "chemical", "pesticide", "toxic", "solvent"],
        "Textile": ["shirt", "cloth", "fabric", "jeans", "textile", "towel"],
        "Composite": ["tetra", "blister", "carton", "multi-layer", "chip bag"]
    }

def match_material_from_keywords(description: str) -> str:
    """
    Tries to match the input description to a material type using keyword taxonomy.
    This acts as a supporting classifier for more robust classification.
    """
    taxonomy = get_taxonomy_keywords()
    desc = description.lower()

    for material, keywords in taxonomy.items():
        if any(word in desc for word in keywords):
            return material

    return "Unknown"
