import pytest
pytestmark = pytest.mark.unit


# ⚠️ adapte l'import selon ton projet
# ex: from app.predict import predict_water
from app.predict import predict_water

class DummyModel:
    def predict(self, features):
        return 2.3

def test_prediction_expected(monkeypatch):
    monkeypatch.setattr("app.predict.load_model", lambda: DummyModel())

    features = {"weight": 70, "age": 25, "activity_level": "medium"}
    pred = predict_water(features)

    assert isinstance(pred, (int, float))
    assert round(pred, 2) == 2.30
