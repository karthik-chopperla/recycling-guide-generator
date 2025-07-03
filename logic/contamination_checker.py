# logic/contamination_checker.py

def check_for_contamination(description: str) -> (str, str):
    """
    Analyzes item description to determine contamination status and reason.
    Returns:
    - contamination_level: Clean / Contaminated / Highly Contaminated
    - reason: Context-specific explanation (brief)
    """
    desc = description.lower()

    # Keyword groups
    curry_related = ["curry", "gravy", "sabzi", "masala", "dal"]
    rice_related = ["rice", "biryani", "fried rice", "leftover rice"]
    dairy_related = ["milk", "curd", "yogurt", "paneer", "cheese", "buttermilk"]
    grease_related = ["grease", "greasy", "butter", "ghee", "oil", "oily"]
    vegetable_related = ["vegetable", "peels", "boiled", "uncooked", "raw", "salad"]
    crumb_related = ["crumbs", "scrap", "leftover", "bite", "half-eaten"]
    wet_related = ["wet", "soaked", "stained", "liquid", "moist"]
    general_spoilage = ["spoiled", "rotten", "stale", "smelly", "fungus", "mold"]

    level = "Clean"
    reason = "No contamination detected."

    if any(word in desc for word in curry_related):
        level = "Highly Contaminated"
        reason = "Contains curry-based oily/spiced residue."

    elif any(word in desc for word in dairy_related):
        level = "Highly Contaminated"
        reason = "Contains dairy residue which spoils fast."

    elif any(word in desc for word in rice_related):
        level = "Contaminated"
        reason = "Contains fermentable starchy food (rice)."

    elif any(word in desc for word in grease_related):
        level = "Contaminated"
        reason = "Grease or oil present — contaminates recyclables."

    elif any(word in desc for word in vegetable_related):
        level = "Contaminated"
        reason = "Vegetable matter introduces decay/moisture."

    elif any(word in desc for word in wet_related):
        level = "Contaminated"
        reason = "Wet or stained item reduces recyclability."

    elif any(word in desc for word in crumb_related):
        level = "Contaminated"
        reason = "Contains leftover food crumbs or bites."

    elif any(word in desc for word in general_spoilage):
        level = "Contaminated"
        reason = "Spoiled or moldy item — unsafe for recycling."

    return level, reason
