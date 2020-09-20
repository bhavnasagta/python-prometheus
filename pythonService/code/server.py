import json
import time
import flask
import requests
from config import config
from werkzeug.exceptions import HTTPException

from flask import Flask, Response, request, abort, jsonify, request
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, Gauge
from prometheus_client import Summary, Counter, Histogram


FLASK_REQUEST_LATENCY = Histogram('http_request_duration_seconds',
                                  'Flask Request Latency',
                                  ['up', 'route', 'group'])


def before_request():
    request.start_time = time.time()


def after_request(response):
    if str(response.status_code).startswith("2"):
        status_code = "2XX"
    if str(response.status_code).startswith("3"):
        status_code = "3XX"
    if str(response.status_code).startswith("4"):
        status_code = "4XX"
    if str(response.status_code).startswith("5"):
        status_code = "5XX"

    request_latency = time.time() - request.start_time
    return response


def service_call():
    startTime = time.time()
    response = requests.get("https://httpstat.us/200") 
    diffTime = time.time()-startTime
    up = 0
    if (response.status_code) == 200:
        up=1 
    FLASK_REQUEST_LATENCY.labels(up, "https://httpstat.us/200", config["service_name"]).observe(diffTime)
    startTime = time.time()
    response = requests.get("https://httpstat.us/503") 
    diffTime = time.time()-startTime
    up = 0
    if (response.status_code) == 200:
        up=1 
    FLASK_REQUEST_LATENCY.labels(up, "https://httpstat.us/503", config["service_name"]).observe(diffTime)
    return



def monitor(app):
    app.before_request(before_request)
    app.after_request(after_request)


app = flask.Flask(__name__)
monitor(app)


@app.route('/'+config["service_name"]+"/health", methods=['GET'])
@app.route('/'+config["service_name"]+"/"+config["service_version"]+'/health', methods=['GET'])
def health():

    response = dict()
    response['success'] = "success"
    return flask.jsonify(response)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


@app.route('/'+"metrics", methods=['GET'])
def metrics():
    service_call()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)