from flask import Flask, jsonify, request
from datetime import datetime
import io
import sys
import numpy as np

app = Flask(__name__)

@app.route('/')
def aeo_function():
    firstname = request.args.get('firstname', 'World')
    familyname = request.args.get('familyname', 'World')
    date_time = datetime.now()

    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(firstname)
        status = sys.stdout.getvalue()
    except Exception as e:
        status = str(e)
    finally:
        sys.stdout = stdout_backup

    data = {'message': f'Hello {firstname} {familyname}!',
            'date': date_time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': status}

    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
