import os
from flask import Flask, jsonify
from pymongo import MongoClient

# Initialiser l'application Flask
app = Flask(__name__)

# Recuperer l'URI de connexion depuis les variables d'environnement
# 'mongodb' correspond au nom du service defini dans le fichier docker-compose.yml
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/testdb")

# Initialiser la connexion au client MongoDB
client = MongoClient(MONGO_URI)
db = client.get_default_database()
visits_collection = db["visits"]

# Definir la route principale pour tester la connexion et l'insertion
@app.route('/')
def hello_world():
    try:
        # Inserer un enregistrement de visite dans la collection MongoDB
        visits_collection.insert_one({"status": "connected"})
        count = visits_collection.count_documents({})
        return jsonify({
            "message": "Connexion reussie a MongoDB !",
            "total_visites": count
        })
    except Exception as e:
        # Retourner l'erreur rencontree en cas d'echec de connexion
        return jsonify({
            "message": "Echec de connexion a MongoDB",
            "erreur": str(e)
        }), 500

# Demarrer le serveur Flask sur le port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)