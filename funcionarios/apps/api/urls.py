from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from apps.core.views import (LoginAuthToken,
                             ObtainAuthToken,
                             UserCreateViewSet)
from apps.funcionario.views import EmployeeViewSet, search_cep

router = routers.DefaultRouter()

router.register(r'funcionario', EmployeeViewSet)

helper_patterns = [
    path('', include('rest_framework.urls',
                     namespace='rest_framework')),
    path('user/', UserCreateViewSet.as_view(), name='user'),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('authenticate/',
         LoginAuthToken.as_view(),
         name='authenticate'),
    path('cep/<str:cep>/', search_cep, name='cep')
]

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = helper_patterns
urlpatterns.extend(router.urls)
