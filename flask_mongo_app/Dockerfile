# Utiliser une image Python officielle legere
FROM python:3.9-slim

# Definir le repertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dependances
COPY requirements.txt .

# Installer les dependances necessaires sans utiliser de cache
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application
COPY app.py .

# Exposer le port sur lequel l'application s'execute
EXPOSE 5000

# Commande pour demarrer l'application Flask
CMD ["python", "app.py"]