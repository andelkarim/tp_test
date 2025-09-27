# Utilise une image Python 3.11 légère comme base
FROM python:3.11-slim

# Définit l'application Flask et le mode d'exécution
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier de dépendances et les installe.
# Cela tire parti de la mise en cache de Docker si seuls les requirements changent.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code source de l'application
COPY . .

# Expose le port par défaut de Flask
EXPOSE 5000

# Commande pour démarrer l'application de manière robuste
# Assurez-vous d'avoir 'gunicorn' dans votre requirements.txt.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]