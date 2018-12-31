from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import requests


def get_cep(request, cep):

    address = requests.get(settings.BASE_URL.format(cep))
    return JsonResponse(address.json())
