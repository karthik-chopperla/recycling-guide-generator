# ui/input_form.py

import streamlit as st

def get_user_input() -> str:
    """
    Render input field for user to enter item description.
    Returns cleaned text input.
    """
    st.markdown("Enter a short description of the item you want to recycle:")
    user_input = st.text_input("Example: 'pizza box with grease stains', 'foil packet with leftover rice', 'old charger'")
    return user_input.strip()
