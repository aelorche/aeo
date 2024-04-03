from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute-python', methods=['POST'])
def execute_python_code():
    code = request.json.get('code')
    # Exécuter le code Python (attention à la sécurité!)
    result = execute_code_safely(code)
    # Renvoyer les résultats dans la réponse
    return jsonify({'result': result}), 200

def execute_code_safely(code):
    # Exécutez le code de manière sécurisée (par exemple, en utilisant sandboxing)
    # Cela peut nécessiter l'utilisation de bibliothèques tierces comme PySandbox
    # Pour cet exemple, nous allons simplement simuler le traitement du code
    result = eval(code)
    return result

if __name__ == '__main__':
    app.run(debug=True)
