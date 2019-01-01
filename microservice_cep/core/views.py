from flask_restful import Resource
from flask import Flask, abort
from microservice_cep.core.serializers import AddressSchema
import requests
import json


BASE_URL = 'http://viacep.com.br/ws/{}/json/'


class BuscaCep(Resource):

    def get(self, cep):

        address = requests.get(BASE_URL.format(cep))
        address = json.loads(address.text)
        address = AddressSchema().load(address)

        json_data, error = AddressSchema().dump(address.data)

        if error:
            abort(404)

        return json_data
