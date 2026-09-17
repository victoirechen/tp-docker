from flask import Flask

# Initialiser l'application Flask
app = Flask(__name__)

# Definir la route principale qui renvoie un message simple
@app.route('/')
def hello_world():
    return 'Hello, World from Dockerized Flask!'

# Demarrer le serveur sur toutes les interfaces (0.0.0.0) sur le port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)