#!/usr/bin/python

import cx_Oracle
from flask import Flask, jsonify, request, render_template
import json
import time
import logging
from flask import request
import jsonschema
import os

LOG_LEVEL="INFO"

if  os.environ.get('LOG_LEVEL'):
    LOG_LEVEL=os.environ.get('LOG_LEVEL')

LOG_NUM_SEV = getattr(logging,LOG_LEVEL.upper(),logging.INFO)


logging.basicConfig(level=LOG_NUM_SEV)
logging.debug('Started')

app = Flask(__name__)

def run_select(user, password, db_host, db_port, instanse, query):
    start_time = time.time()
    return_data = {
        'oracle_status': '',
        'query': query,
        'result': [],
        'count': 0,
        'execution_time': 0
    }
    logging.debug('Executing: run_select with args:', user, password, db_host, db_port, instanse, query  )
    cursor = None
    try:
        #connect to database and execute query.
        db = cx_Oracle.connect(user, password, db_host+":"+str(db_port)+"/" + instanse)
        cursor = db.cursor()
        cursor.execute(query) 
        for row in cursor:
            return_data['result'].append(row)
    except (cx_Oracle.DatabaseError, cx_Oracle.InterfaceError) as exc:
        error, = exc.args
        return_data['oracle_status'] = error.code
        return_data['error_msg'] = error.message
    finally:
        if cursor:
            cursor.close()

    end_time = time.time()
    return_data['count'] = len(return_data['result'])
    return_data['execution_time'] = end_time - start_time
    return return_data



@app.route('/info')
def get_info():
    info = {
        "ORA_CLIENT_VERSION": os.environ.get('ORA_CLIENT_VERSION'),
        "PYTHON_VERSION": os.environ.get('PYTHON_VERSION'),
        "ORA_API_VERSION":os.environ.get('ORA_API_VERSION')
    }
    return jsonify(info)


@app.route('/api/v1/select' , methods=['POST'])
def select():
    data = request.get_json()
    try:
    # Validate the user request format
        with open('/opt/data/api/ORA_API_schema.json') as data_file:
            load_schema = json.loads(data_file.read())
        jsonschema.validate(data, load_schema)
    except jsonschema.exceptions.ValidationError as exception:
        error_msg = "Issue with Input json data" + exception.message.replace("u'", "'")
        return jsonify({"error_msg": error_msg}), 400

    query = data['query']
    return_data = run_select(data['User'], data['password'], data['db_host'], data['db_port'], data['instance'], query)
    logging.debug('Return select query:', return_data )
    return jsonify(return_data)
    



if __name__ == '__main__':
    app.run(host='0.0.0.0')
