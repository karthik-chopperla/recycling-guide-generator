# logic/simulation_rules.py

import random

def simulate_regional_rules():
    """
    Simulate basic recycling rules for a region to mimic dynamic policy handling.
    This is logic-based simulation, no static data.
    """
    rules = {
        "Plastic": random.choice(["Accepted", "Rejected"]),
        "Glass": random.choice(["Accepted", "Rejected"]),
        "Paper": "Accepted",
        "Metal": "Accepted",
        "E-Waste": "Special Center Only",
        "Organic": "Compost Only",
        "Hazardous": "Hazmat Pickup Required",
        "Textile": random.choice(["Donation Preferred", "Special Drop-off"]),
        "Composite": "Landfill (Non-Recyclable)"
    }
    return rules


def simulate_regional_policy(description: str) -> str:
    """
    Returns region-specific recycling guidance simulation
    based on keywords in item description.
    """
    desc = description.lower()

    if "india" in desc or "kerala" in desc:
        return "In India, organic waste can be composted or placed in green bins if available. Informal recycling is also common."

    elif "germany" in desc:
        return "In Germany, use the 'Bioabfall' bin for organic waste. Strict separation rules apply to paper, plastic, and e-waste."

    elif "usa" in desc or "california" in desc:
        return "In the USA, recycling rules vary by county. Electronics should go to certified e-waste collection centers."

    elif "uk" in desc:
        return "In the UK, separate recyclables into council bins. Organic waste may go into a brown or food bin."

    return ""
