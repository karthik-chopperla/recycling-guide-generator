# logic/contamination_reasoner.py

def generate_contamination_reason(description: str, material: str) -> str:
    """
    Generates explanation for contamination, based on detected material and description.
    Only returns reason if relevant. Avoids mismatched logic.
    """
    desc = description.lower()
    mat = material.lower()

    if "curry" in desc or "grease" in desc:
        if "plastic" in mat:
            return "Food residue prevents proper plastic recycling."
        elif "paper" in mat:
            return "Grease prevents paper fibers from separating."
        elif "metal" in mat:
            return "Metal contaminated with food may be rejected."
        elif "composite" in mat:
            return "Multi-layered packaging with food can't be separated cleanly."
        elif "glass" in mat:
            return "Glass with food residue must be rinsed before recycling."

    return ""  # No contamination reason needed
