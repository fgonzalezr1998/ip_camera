#! /usr/bin/env python3

import sys
import time
from CameraServer import CameraServer
from flask import Flask, jsonify

app = Flask("IP_Camera_Server")
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