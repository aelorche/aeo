from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Your data
    data = {'message': 'Hello, world!'}

    # Setting Content-Type header to 'application/json'
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
