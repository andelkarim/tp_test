from flask import Flask
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os
from .db import init_app, init_db
from . import main

load_dotenv()

def create_app():
    app = Flask(__name__)

    # clé, CSRF, routes
    app.secret_key = os.getenv('SECRET_APP', 'noneAZERTY')
    CSRFProtect(app)
    app.register_blueprint(main.bp)

    # Contexte applicatif
    with app.app_context():
        # ⚠️ Ne lance PAS la DB si on est en mode test unit/UI
        # (utilisé par la CI: SKIP_DB_INIT=1)
        if os.getenv("SKIP_DB_INIT") != "1":
            init_db()
        # init_app peut enregistrer les teardown/cli etc.
        init_app(app)

    return app

# On garde 'app' pour les lanceurs (flask run / gunicorn / uvicorn)
app = create_app()
