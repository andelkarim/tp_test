import pytest
import numpy as np
from app.predict import predict_water

pytestmark = pytest.mark.unit


def test_prediction_expected():
    # Entrées stables et valides pour la fonction: deux séries numériques
    sleeptime = [7, 8, 6.5]  # heures de sommeil
    steps = [8000, 9500, 10000]  # nombre de pas

    pred = predict_water(sleeptime, steps)

    # Valeur attendue calculée avec la même formule que dans l'app
    expected = 0.002 * np.average(sleeptime) + 0.009 * np.average(steps)

    assert isinstance(pred, (int, float))
    assert pred == pytest.approx(expected, rel=1e-6)
