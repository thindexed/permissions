import logging
import json
import pathlib

from flask import Flask, request, jsonify

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

print(__package__)
data_anonym = json.loads(pathlib.Path(__file__).parent.joinpath('permissions-anonym.json').read_text())
data_admin = json.loads(pathlib.Path(__file__).parent.joinpath('permissions-admin.json').read_text())
data_user = json.loads(pathlib.Path(__file__).parent.joinpath('permissions-user.json').read_text())

@app.route('/permissions')
def permissions():
    role = request.headers.get('x-role')   
    print("role:", role)     
    if role == "admin":
        return jsonify(data_admin)

    if role == "user":
        return jsonify(data_user)

    return jsonify(data_anonym)

if __name__ == '__main__':
    print("AuthZ Server Up and running")
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)


