from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute-python', methods=['GET'])
def execute_python_code():
    python_code = request.form.get('python_code')
    
    try:
        result = eval(python_code)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
