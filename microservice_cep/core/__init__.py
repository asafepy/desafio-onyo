import json

from flask import Flask, abort
from flask_restful import Resource, Api

from .views import BuscaCep

app = Flask(__name__)
api = Api(app)

api.add_resource(BuscaCep, '/ws/<string:cep>/')