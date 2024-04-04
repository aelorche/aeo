from flask import Flask, jsonify, request
from datetime import datetime
import io
import sys
import numpy as np

app = Flask(__name__)

@app.route('/')
def python_code():
    code = request.args.get('code', 'code')
    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code)
        output_result = sys.stdout.getvalue()
        output_type = 'S'
    except Exception as e:
        output_result = str(e)
        output_type = 'E'
    finally:
        sys.stdout = stdout_backup

    data = {'output_result': output_result, 'output_type': output_type}

    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
