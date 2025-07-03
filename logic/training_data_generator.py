# logic/training_data_generator.py

import random

def generate_training_data(n=100):
    """
    Generates synthetic item descriptions and labels for material type classification.
    """
    samples = []
    materials = {
        "Plastic": ["bottle", "plastic bag", "poly wrap", "toothbrush"],
        "Glass": ["glass jar", "wine bottle", "mirror", "bulb"],
        "Paper": ["newspaper", "magazine", "cardboard", "paper bag"],
        "Metal": ["tin can", "aluminum foil", "steel rod"],
        "E-Waste": ["laptop", "mobile phone", "battery", "charger"],
        "Organic": ["banana peel", "vegetable waste", "leftover food"],
        "Hazardous": ["paint can", "pesticide", "chemical bottle"],
        "Textile": ["cotton shirt", "old jeans", "fabric scrap"],
        "Composite": ["tetra pack", "blister pack", "chip bag"]
    }

    for _ in range(n):
        label = random.choice(list(materials.keys()))
        desc = random.choice(materials[label])
        samples.append((desc, label))
    
    return samples
