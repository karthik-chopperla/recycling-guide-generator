# tests/test_ui.py

# Streamlit UI elements are hard to test directly.
# We test utility behavior or simulate input/output logic.

from ui.result_display import show_results

def test_show_results_display():
    # Dummy test to simulate function usage
    try:
        show_results("Plastic", "Recycle clean plastic", "Accepted", 0.95)
        passed = True
    except Exception:
        passed = False
    assert passed
