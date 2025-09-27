import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_summary_display(client):
    resp = client.get("/summary")
    assert resp.status_code == 200

    # Si c'est du JSON
    try:
        data = resp.get_json()
        if data is not None:
            assert "total_activities" in data or "activities" in data
            assert "total_distance_km" in data or "distance" in data
            return
    except Exception:
        pass

    # Sinon on teste l'HTML
    html = resp.data.decode().lower()
    assert ("résumé" in html) or ("summary" in html)
    assert ("km" in html) or ("distance" in html)
