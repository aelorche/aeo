from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('name', 'World')
    date_time = datetime.now()

    if (name = 'Ahmed'):
        status = "NOK"
    else
        status = "NOK"
    
    data = {'message': f'Hello {name}!',
            'date':date_time,
            'status':status}

    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
