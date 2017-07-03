#!/usr/bin/python3
from flask import Flask, request, json, Response
from MongoDao import MongoDao
from bson import json_util
import os

app = Flask(__name__)
logger = app.logger
dao = None;
@app.route("/health")
def health():
    logger.debug("Get Health");
    return json.jsonify(healthy='true');

if __name__ == "__main__":
    dao = MongoDao("mongodb://test:test@ds063856.mlab.com:63856/auth");
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
