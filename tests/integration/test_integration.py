# Fichier : tests/test_integration.py

import pytest
from app import create_app
from app.db import get_db, init_db
import subprocess
import time


@pytest.fixture(scope="module")
def db_server():
    # Lancer le serveur de base de données comme dans init-env.sh
    process = subprocess.Popen(["sh", "init-env.sh"])
    time.sleep(10)  # Laisser le temps au serveur de démarrer
    yield
    process.terminate()


@pytest.fixture()
def app(db_server):
    app = create_app()
    with app.app_context():
        # S'assurer que la BDD est initialisée avant chaque test
        init_db()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_request_log_form(client):
    response = client.get("/log")
    assert b"Log Activity" in response.data


# Nouveau test à ajouter
def test_user_activity_summary(client):
    # Insérer des données de test directement dans la base de données
    with client.application.app_context():
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute(
                "INSERT INTO activities (userid, logday, sleeptime, steps, water) VALUES (%s, %s, %s, %s, %s)",
                (999, "2025-01-01", 8, 10000, 2000),
            )
        db.commit()

    # Faire une requête pour le résumé des activités de l'utilisateur 999
    response = client.get("/user/999")

    # Vérifier que la réponse est correcte
    assert response.status_code == 200
    assert b"User Activity" in response.data
    assert b"999" in response.data  # Vérifier que l'ID utilisateur est affiché
    assert b"8" in response.data  # Vérifier que les données sont affichées
    assert b"10000" in response.data
    assert b"2000" in response.data
