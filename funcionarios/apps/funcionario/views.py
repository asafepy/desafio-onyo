import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models.funcionario import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


def search_cep(request, cep):
    address = requests.get(settings.BASE_URL.format(cep))
    print(address.status_code)
    if address.status_code == 200:
        return JsonResponse(address.json())

    return JsonResponse({'message':'CEP não localizado!'}, status=404)
