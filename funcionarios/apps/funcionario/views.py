from rest_framework.views import APIView
from rest_framework.response import Response
from apps.funcionario.models.funcionario import Employee
from apps.funcionario.models.endereco import Address
from rest_framework import viewsets
from .serializers import EmployeeSerializer, AddressSerializer


class EmployeeViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class AddressViewSet(viewsets.ModelViewSet):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()
