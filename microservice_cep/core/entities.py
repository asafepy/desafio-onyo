

class Address:
    def __init__(self, cep, bairro, localidade, logradouro, uf):
        self.cep = cep
        self.bairro = bairro
        self.logradouro = logradouro
        self.localidade = localidade
        self.uf = uf

    def __repr__(self):
        return '<Address(localidade={self.localidade!r})>'.format(self=self)
