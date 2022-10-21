from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
import json


app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

USER_DATA = { "admin" : "superAdmin" }
with open("config.json") as f:
    CONFIGS = json.load(f)


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


@app.route('/api/v1/config', methods=['POST'])
@auth.login_required
def downloadConfig():
    id = request.form.get('identifier')
    if id in CONFIGS:
        return CONFIGS.get(id)




if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')