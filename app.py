#!/usr/bin/env python
'''Provide mock data for Policy Search that returns JSON'''

from flask import Flask, Response, json, jsonify, request
from flask_cors import CORS, cross_origin
from functools import wraps
app = Flask(__name__)
CORS(app)

mock_data =[
    {
        "policy": "N35111111",
        "status": "endorsement",
        "state": "OK"
    },
    {
        "policy": "N24777777",
        "status": "rewrite",
        "state": "MO"
    },
    {
        "policy": "N03555555",
        "status": "renewal",
        "state": "AR"
    }
]


@app.route('/')
def hello_world():
    '''Obligatory Hello, World!'''
    return 'Hello, World!'


@app.route('/echo', methods=['GET', 'POST'])
def echo():
    '''Echo request variables for testing'''
    if request.method == 'POST':
        jsonbody = json.load(request.stream)
        return jsonify({
            'result': repr(jsonbody)
        })
    elif request.method == 'GET':
        return jsonify({
            'result': request.args
        })
    else:
        return jsonify({'result': request.args.get('result', 'No POST or GET variables sent')})


@app.route('/policy-search/api/v1.0/policies', methods=['GET', 'POST'])
def get_policies():
    '''Return policies that meet the search criteria'''
    return jsonify(mock_data)


if __name__ == '__main__':
    app.run()
