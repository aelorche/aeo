from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Accessing request.json inside the request handler function
    datain = request.json
    name = datain.get('input', 'Ahmed')
    
    data = {'message': f'Hello, {name}!'}

    # Setting Content-Type header to 'application/json'
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
