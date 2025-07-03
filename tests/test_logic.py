# tests/test_logic.py

from logic.material_classifier import MaterialClassifier
from logic.disposal_guidance import DisposalGuidance
from logic.simulation_rules import simulate_regional_rules
from logic.training_data_generator import generate_training_data

def test_material_classifier():
    classifier = MaterialClassifier()
    result = classifier.classify("used plastic bottle")
    assert result in classifier.material_types

def test_disposal_guidance():
    guidance = DisposalGuidance()
    message = guidance.get_guidance("Plastic")
    assert "plastic" in message.lower()

def test_simulation_rules():
    rules = simulate_regional_rules()
    assert isinstance(rules, dict)
    assert "Plastic" in rules

def test_training_data_generator():
    data = generate_training_data(10)
    assert len(data) == 10
    for desc, label in data:
        assert isinstance(desc, str)
        assert isinstance(label, str)
