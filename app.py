from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('name', 'World')

    name_out = name
    date = sysdate
    status = "OK"
    
    data = {'message': f'Hello {name}!',
            'date':sysdate,
            'status':status}

    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
