from rest_framework import serializers
from apps.funcionario.models.funcionario import Employee
from apps.funcionario.models.endereco import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('cep', 'bairro', 'localidade', 'uf')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Employee
        fields = ('url', 'id', 'name', 'surname', 'role', 'address')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)

        address.save()

        instance = Employee.objects.create(**validated_data, address=address)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')

        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.role = validated_data.get('role', instance.role)
        instance.address.cep = address_data['cep']
        instance.address.bairro = address_data['bairro']
        instance.address.localidade = address_data['localidade']
        instance.address.uf = address_data['uf']

        instance.address.save()
        instance.save()

        return instance
