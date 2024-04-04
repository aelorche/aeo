@app.route('/')
def aeo_function():
    firstname = request.args.get('firstname', 'World')
    familyname = request.args.get('familyname', 'World')
    date_time = datetime.now()

    # Redirect stdout to a StringIO object to capture the print output
    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    try:
        # Execute the code passed as a string
        exec(firstname)
        status = sys.stdout.getvalue()
    except Exception as e:
        status = str(e)
    finally:
        # Restore stdout
        sys.stdout = stdout_backup

    data = {'message': f'Hello {firstname} {familyname}!',
            'date': date_time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': status}

    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'

    return response
