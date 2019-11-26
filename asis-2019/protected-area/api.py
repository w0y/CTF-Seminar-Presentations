from flask import current_app as app
from flask import request, render_template, send_file
from .functions import *
from config import *
import os

@app.route('/check_perm/readable/', methods=['GET'])
def app_check_file() -> str:
    try:
        file = request.args.get("file")

        file_path = os.path.normpath('application/files/{}'.format(file))
        with open(file_path, 'r') as f:
            return str(f.readable())
    except:
        return '0'

@app.route('/read_file/', methods=['GET'])
def app_read_file() -> str:
    
    file = request.args.get("file").replace('../', '')
    qs = request.query_string.decode('UTF-8')

    if qs.find('.txt') != (len(qs) - 4):
        return 'security'
    
    try:
        return send_file('files/{}'.format(file))
    except Exception as e:
        return "500"

@app.route('/protected_area_0098', methods=['GET'])
@check_login
def app_protected_area() -> str:
    return Config.FLAG

@app.route('/', methods=['GET'])
def app_index() -> str:
    return render_template('index.html')

@app.errorhandler(404)
def not_found_error(error) -> str:
    return "Error 404"