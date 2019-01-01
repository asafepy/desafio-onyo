from datetime import date
from marshmallow import Schema, fields, post_load
from microservice_cep.core.entities import Address


class AddressSchema(Schema):

    cep = fields.Str(allow_none=True)
    bairro = fields.Str(allow_none=True)
    localidade = fields.Str(allow_none=True)
    logradouro = fields.Str(allow_none=True)
    uf = fields.Str(allow_none=True)

    @post_load
    def make_object(self, data):
        return Address(**data)
