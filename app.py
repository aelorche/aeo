from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def aeo_function():
    firstname = request.args.get('firstname', 'World')
    familyname = request.args.get('familyname', 'World')
    date_time = datetime.now()

    
    status = eval("print('hello Ahmed')")
    
    data = {'message': f'Hello {firstname} {familyname}!',
            'date': date_time,
            'status': status}

    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
