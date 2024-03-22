from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

# Chargez les variables d'environnement
app.config['DEBUG'] = os.getenv('FLASK_DEBUG') == 'True'

@app.route('/', methods=['GET'])
def hello_name():
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400

    name = data.get('input', 'World')
    number_1 = data.get('number_1', '1')
    number_2 = data.get('number_2', '2')
    
    try:
        number_3 = int(number_1) + int(number_2)
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

    response = {'message': f'Hello, {name}!', 'number_1 + number_2':  f'{number_3}'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
