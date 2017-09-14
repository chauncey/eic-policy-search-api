#!/usr/bin/env python
'''Provide mock data for Policy Search that returns JSON'''

from flask import Flask, Response, json, jsonify, request
from functools import wraps
app = Flask(__name__)


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


def get_fakedata():
    fake = {'status': 'good', 'pol': u'N11111111', 'session': sess,
            'billing': {'status': 'Installment Billed ', 'mindue': '$131.00', 'accept': 'I',
                        'fulldue': '$778.15', 'cancdate': '07/12/2013', 'exp': '101213',
                        'duedate': '06/27/2013'},
            'policy': {'prem': '$891.00', 'exp': '10/12/2013',
                       'name': u'DOE, JACK &/OR JANE', 'eff': '06/12/2013',
                       'agpinfo': {'ephone': '555-333-8888',
                       'email': u'noreply@equityins.net', 'dphone': '555-345-6789'}},
            'drivers': [{'name': u'DOE,JACK', 'lic': '****9101', 'dob': '11/11/1973',
                         'marry': 'Married', 'licst': u'OK', 'sex': 'Male'},
                        {'name': u'DOE,JANE', 'lic': '****5110', 'dob': '07/04/1971',
                         'marry': 'Married', 'licst': u'OK', 'sex': 'Female'},
                        {'name': u'DOE,CASEY', 'lic': '****1197', 'dob': '09/08/1993',
                         'marry': 'Single', 'licst': u'OK', 'sex': 'Female'}],
            'vehicles': [{'index': u'1', 'make': u'HOND', 'vin': u'11111111111111111',
                          'um': '25', 'pd': '25', 'model': u'ACCORD', 'bi2': '50', 'bi1': '25'},
                         {'index': u'2', 'make': u'DODG', 'vin': u'22222222222222222', 'um': '25',
                          'pd': '25', 'model': u'CARAVAN', 'bi2': '50', 'bi1': '25'},
                         {'index': u'3', 'make': u'FORD', 'vin': u'33333333333333333', 'um': '25',
                          'pd': '25', 'model': u'WINDSTAR', 'bi2': '50', 'bi1': '25'},
                         {'index': u'4', 'make': u'CHEV', 'vin': u'44444444444444444', 'um': '25',
                          'pd': '25', 'model': u'MALIBU', 'bi2': '50', 'bi1': '25'}],
            'excl': [],
            'agent': {'phone': '918-111-2222', 'fax': '918-333-4444',
                      'addr2': u'6145 E 21 ST', 'zip': u'74114', 'cityst': 'Tulsa, OK',
                      'addr1': u'', 'agency': u'AAA INSURANCE AGENCY', 'email': ''},
            'decs': [{'pdate': '03/15/2013', 'pdftag': '(pdf)', 'ptype': 'Endorsement', 'pfile': '/archivepdfs/IRF201303151354EUW_N11111111_50000_ENDR_20130315_DOE,JAKE@ORJANE_03151354.pdf'}]
            }
    return fake


def jsonp(data, callback="function"):
    '''Provide a JSONP response with callback'''
    return Response(
        "%s(%s);" %(callback, json.dumps(data)),
        mimetype="text/javascript"
    )


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
    if request.method == 'GET':
        callback = request.args.get('callback')
        if callback:
            return jsonp(mock_data, callback)
        else:
            return jsonp(mock_data)


@app.route('/m/applogin', methods=['POST'])
def login():
    if request.method == 'POST':
        jsonbody = json.load(request.stream)
        print jsonbody
        return jsonify([get_fakedata()])


if __name__ == '__main__':
    app.run()
