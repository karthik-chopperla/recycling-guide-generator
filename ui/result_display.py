# ui/result_display.py

import streamlit as st

def show_results(material_type: str,
                 contamination_level: str,
                 contamination_reason: str,
                 confidence: dict,
                 guidance: str):
    """
    Displays the output results to the user in Streamlit.
    """
    st.markdown("## ♻️ Recycling Analysis Results")

    st.markdown(f"**Predicted Material Type:** `{material_type}`")
    st.markdown(f"**Contamination Level:** `{contamination_level}`")

    if contamination_level != "Clean":
        st.markdown(f"**Reason for Contamination:** {contamination_reason}")

    st.markdown(f"**Material Match Confidence:** `{confidence['material_confidence']}%`")
    st.markdown(f"**Guidance Confidence Level:** `{confidence['guidance_confidence']}`")
    st.markdown(f"**Why Confidence Score:** {confidence['reason']}")

    st.markdown("### 🗑️ Recycling Guidance")
    st.info(guidance)
