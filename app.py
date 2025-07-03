import streamlit as st

# Logic modules
from logic.material_classifier import classify_material
from logic.contamination_checker import check_for_contamination
from logic.contamination_reasoner import generate_contamination_reason
from logic.confidence_estimator import estimate_confidence
from logic.disposal_guidance import DisposalGuidance
from logic.simulation_rules import simulate_regional_policy
from logic.abstract_checker import is_non_recyclable_input

# ML & UI
from ml.evaluator import evaluate_classifier_performance
from ui.result_display import show_results
from ui.input_form import get_user_input
from utils.helpers import clean_text
from data.taxonomy_rules import get_taxonomy_keywords

# Initialize
guidance_engine = DisposalGuidance()
taxonomy = get_taxonomy_keywords()

# App Setup
st.set_page_config(page_title="♻️ Recycling Guide Generator", layout="centered")
st.title("♻️ Recycling Guide Generator")

# Input Section
user_input = get_user_input()

if user_input:
    cleaned = clean_text(user_input)

    # Reject abstract or non-object inputs
    if is_non_recyclable_input(cleaned):
        st.error("❌ Please enter a real-world recyclable item or material, not a vague word or concept.")
        st.markdown("**Examples**: 'plastic food wrapper', 'used charger', 'pizza box with grease stains'")
    else:
        # Classification
        material_type, material_confidence, explanation = classify_material(cleaned)

        if material_type in ["Unknown", "Uncertain"]:
            for mat, keywords in taxonomy.items():
                if any(k in cleaned for k in keywords):
                    material_type = mat
                    break

        # Contamination
        contamination_level, _ = check_for_contamination(cleaned)
        contamination_reason = generate_contamination_reason(cleaned, material_type)

        # Confidence Estimate
        confidence = estimate_confidence(cleaned, material_type)

        # Guidance
        guidance = guidance_engine.get_guidance(material_type)

        # Regional Adjustment
        region_note = simulate_regional_policy(cleaned)

        # Display
        show_results(
            material_type=material_type,
            contamination_level=contamination_level,
            contamination_reason=contamination_reason,
            confidence=confidence,
            guidance=guidance
        )

        if region_note:
            st.markdown(f"**🌍 Regional Policy Simulation:** {region_note}")

        st.markdown("---")
        st.markdown("### 🧪 Classification Model Simulation Report")
        evaluate_classifier_performance()
