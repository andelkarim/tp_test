import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

@pytest.mark.integration  # marque ce test comme intégration sans changer le marqueur du fichier
def test_summary_display(client):
    resp = client.get("/summary")
    assert resp.status_code == 200

    # Accepte JSON ou HTML selon ton implémentation
    if resp.is_json:
        data = resp.get_json()
        # adapte ces clés si besoin
        assert "total_activities" in data
        assert "total_distance_km" in data
    else:
        html = resp.data.decode().lower()
        assert ("résumé" in html) or ("summary" in html)
        assert ("km" in html) or ("distance" in html)
