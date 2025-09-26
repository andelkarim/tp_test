import pytest
pytestmark = pytest.mark.integration

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_summary_display(client):
    """
    Vérifie que l'endpoint /summary renvoie bien le résumé attendu.
    """
    response = client.get("/summary")
    assert response.status_code == 200

    if response.is_json:
        data = response.get_json()
        assert "total_activities" in data
        assert "total_distance_km" in data
    else:
        html = response.data.decode().lower()
        assert "résumé" in html or "summary" in html
        assert "km" in html or "distance" in html