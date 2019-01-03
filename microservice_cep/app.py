import json

from flask import Flask, abort
from flask_restful import Resource, Api

from microservice_cep.core.views import BuscaCep

app = Flask(__name__)
api = Api(app)

api.add_resource(BuscaCep, '/ws/<string:cep>/')

if __name__ == '__main__':
    app.run(debug=True)