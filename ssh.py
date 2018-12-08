#!/usr/bin/python

import cx_Oracle
import json
import time
import logging
import jsonschema
import os
import re

from flask import Flask, jsonify, request, render_template
import requests

LOG_LEVEL="INFO"

if  os.environ.get('LOG_LEVEL'):
    LOG_LEVEL=os.environ.get('LOG_LEVEL')

app = Flask(__name__)

@app.route('/info')
def get_info():
    info = {
        "TARGET_MACHINE": ,
        "TARGET_USER": ,
        "TARGET_USER_PASSWORD":,
        "SOURCE_MACHINE": ,
        "SOURCE_USER": ,
        "SOURCE_USER_PASSWORD":,
        "IS_SYNCHRONOUS":

    }
    return jsonify(info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')