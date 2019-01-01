from django.db import models
length = 100


class Address(models.Model):

    cep = models.CharField(max_length=length, blank=True, null=True)
    bairro = models.CharField(max_length=length, blank=True, null=True)
    localidade = models.CharField(max_length=length, blank=True, null=True)
    uf = models.CharField(max_length=length, blank=True, null=True)