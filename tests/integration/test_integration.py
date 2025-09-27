import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update(TESTING=True)
    return app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_request_log_form(client):
    resp = client.get('/log')
    assert resp.status_code == 200
    assert b'Log Activity' in resp.data

def test_summary_display(client):
    resp = client.get('/summary')
    assert resp.status_code == 200
    # on accepte "Summary" ou "Résumé" selon ton template
    body = resp.data.decode().lower()
    assert ('summary' in body) or ('résumé' in body)


# test pr
# test trigger
