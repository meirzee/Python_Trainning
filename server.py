#!/usr/bin/python

import cx_Oracle
from flask import Flask, jsonify, request, render_template
import json
import time
import logging

LOG_LEVEL=""

logging.basicConfig(level=logging.DEBUG)
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
        db = cx_Oracle.connect(user, password, db_host+":"+db_port+"/" + instanse)
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


@app.route('/myhtml')
def index():
   return jsonify(return_data)

# @app.route('/s')
# def select():
#     #return_data = run_select(user, password, db_host, db_port, instanse, query)
#     return render_template('select.html', posts=return_data)
  

@app.route('/api/v1/select' , methods=['POST'])
def select():
    data = request.get_json()
    query = data['query']
    return_data = run_select(data['User'], data['password'], data['db_host'], data['db_port'], data['instance'], query)
    logging.debug('Return select query:', return_data )
    return jsonify(return_data)
    



if __name__ == '__main__':
    app.run(host='0.0.0.0')
