from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

# Chargez les variables d'environnement
app.config['DEBUG'] = os.getenv('FLASK_DEBUG') == 'True'

@app.route('/', methods=['POST'])
def hello_name():
    data = request.json
    name = data.get('input', 'World')  # Obtenez le nom du JSON, ou utilisez 'World' par défaut si non spécifié
    response = {'message': f'Hello, {name}!'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
