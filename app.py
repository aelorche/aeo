from flask import Flask, jsonify, request

app = Flask(__name__)
datain = request.json
@app.route('/')
def hello_world():
    request.headers['Content-Type'] = 'application/json'
    name = datain.get('input', 'Ahmed')
    
    data = {'message': 'Hello, {name}!'}

    # Setting Content-Type header to 'application/json'
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
