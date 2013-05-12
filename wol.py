"""
WOL.py
======
This is a very simple implementation of a RESTful service, designed to wake up
known computers when a request is sent.
"""

from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse
from awake.wol import send_magic_packet
import json

app = Flask(__name__)
api = restful.Api(app)

# For now, we're just using a JSON file of the format:
#  {'computer_name': 'mac-address'}
COMPUTERS = json.load(open('computers.json'))

parser = reqparse.RequestParser()
parser.add_argument('isAwake', type=bool)


class Computer(restful.Resource):
    """
    A Computer only has one attribute: whether or not it is 'awake'.  It'd be
    nice if this was stateful, but the core idea is to just fire a WOL packet
    if the request indicates we should.
    """

    def put(self, name):
        mac_addr = COMPUTERS.get(name, None)
        if mac_addr is None:
            restful.abort(404)

        args = parser.parse_args()
        if args['isAwake'] is True:

            send_magic_packet(mac_addr)
            return {'isAwake': True}, 200

        return {'isAwake': False}, 200


api.add_resource(Computer, '/computer/<string:name>/')

if __name__ == '__main__':
    app.run(debug=True)
