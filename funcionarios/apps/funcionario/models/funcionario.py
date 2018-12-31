from django.db import models
from .endereco import Address
length = 100


class Employee(models.Model):

    name = models.CharField(max_length=length, blank=True, null=True)
    surname = models.CharField(max_length=length, blank=True, null=True)
    role = models.CharField(max_length=length, blank=True, null=True)
    salary = models.FloatField(max_length=length, blank=True, null=True)
    address = models.ForeignKey(
        Address, related_name='address', on_delete=models.CASCADE)
