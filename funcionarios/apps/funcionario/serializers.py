from rest_framework import serializers
from apps.funcionario.models.funcionario import Employee
from apps.funcionario.models.endereco import Address


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ('cep', 'bairro', 'localidade', 'uf')


class EmployeeSerializer(serializers.ModelSerializer):
    
    address = AddressSerializer()

    class Meta:
        model = Employee
        fields = ('name', 'surname', 'role', 'address')

        