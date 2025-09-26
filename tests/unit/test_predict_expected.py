import pytest
from app.predict import predict_water

pytestmark = pytest.mark.unit

def test_prediction_expected():
    # Données d'entrée stables
    features = {"weight": 70, "age": 25, "activity_level": "medium"}

    pred = predict_water(features)

    # On valide un résultat numérique et plausible
    assert isinstance(pred, (int, float))
    # garde une borne large pour rester robuste aux formules internes
    assert 0 < pred < 10
