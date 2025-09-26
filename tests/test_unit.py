from app.predict import predict_water
import pytest
pytestmark = pytest.mark.unit


def test_predict_water_none():
    assert predict_water() is None
