#! /usr/bin/env python3

import sys
import time

from flask import request
from CameraServer import CameraServer
from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin

import modules.db_utils as db

app = Flask("IP_Camera_Server")
cors = CORS(app)
app.config['CORS_HEADERS'] = "Access-Control-Allow-Credentials"
camera_server = CameraServer()

@app.route('/')
def hello():
    return jsonify("Hello World!")

@app.route('/start_capturing')
def start_capturing():
    if (camera_server.start()):
        msg = "SUCCES"
    else:
        msg = "FAILURE"

    return jsonify(msg)

@app.route('/stop_capturing')
def stop_capturing():
    camera_server.stop()
    return jsonify("SUCCESS")

@app.route('/login_check/', methods=['GET', 'POST'])
@cross_origin()
def login_check():

    if (request.method == "GET"):
        user = request.args.get("user")
        psswd = request.args.get("psswd")
        if (db.login_ok(user, psswd)):
            response = jsonify("SUCCESS")
        else:
            response = jsonify("FAILURE")
        return response
    else:
        print("Post")
        return "FAILURE", 401

def start_flask_server():
    app.run(host='0.0.0.0', port=8888, debug=True,  use_reloader=False)

def main(args=None):
    start_flask_server()

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        camera_server.join()
        sys.exit(0)