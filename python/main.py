#! /usr/bin/env python3

import sys
import time

from flask import request
from CameraServer import CameraServer
from flask import Flask, jsonify, Response, render_template
from flask_cors import CORS, cross_origin
import cv2

import modules.db_utils as db

app = Flask("IP_Camera_Server")
cors = CORS(app)
app.config['CORS_HEADERS'] = "Access-Control-Allow-Credentials"
camera_server = CameraServer()

def gen_frames():
    camera_server.start()
    while True:
        ret, buffer = cv2.imencode('.jpg', camera_server.getFrame())
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        time.sleep(0.1)

@app.route('/')
def hello():
    return render_template('main.html')

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
@cross_origin(origin='*',headers=['Content-Type','Authorization', 'Access-Control-Allow-Credentials'])
def login_check():

    if (request.method == "GET"):
        user = request.args.get("user")
        psswd = request.args.get("psswd")
        if (db.login_ok(user, psswd)):
            render_template('main.html')
            response = jsonify("SUCCESS")
        else:
            response = jsonify("FAILURE")
        return response
    else:
        print("Post")
        return "FAILURE", 401

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame')


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