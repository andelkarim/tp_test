# Fichier : tests/test_unit.py
from app.predict import predict_water


def test_predict_water_none():
    assert predict_water() is None


# Nouveau test à ajouter
def test_predict_water_with_data():
    # Définir des données d'entrée, ici une liste pour les moyennes
    sleeptime_data = [6, 8, 7]
    steps_data = [10000, 12000, 9500]

    # Calculer la prédiction attendue selon la formule de predict.py
    # La formule est : 0.002 * np.average(sleeptime) + 0.009 * np.average(steps)
    expected_output = 0.002 * (sum(sleeptime_data) / len(sleeptime_data)) + 0.009 * (
        sum(steps_data) / len(steps_data)
    )

    # Arrondir le résultat pour éviter les problèmes de virgule flottante
    expected_output = round(expected_output, 2)

    # Appeler la fonction de prédiction avec les données
    result = predict_water(sleeptime=sleeptime_data, steps=steps_data)

    # Arrondir le résultat de la fonction de prédiction
    result = round(result, 2)

    # S'assurer que le résultat correspond à l'attente
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
