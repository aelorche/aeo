from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Retrieve input parameter from the request query string
    name = request.args.get('name', 'World')

    # Your data
    data = {'message': f'Hello, {name}!'}

    # Setting Content-Type header to 'application/json'
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
