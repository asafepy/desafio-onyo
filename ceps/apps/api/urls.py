from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from apps.core.views import (LoginAuthToken, 
                             ObtainAuthToken, 
                             UserCreateViewSet)
from apps.cep import views

router = routers.DefaultRouter()

# router.register(r'sensors', views.SensorViewSet)
# router.register(r'equipments', views.EquipamentViewSet)
# router.register(r'equipments_records', views.MeansurementRecordViewSet)

helper_patterns = [
    path('', include('rest_framework.urls', 
                     namespace='rest_framework')),
    path('user/', UserCreateViewSet.as_view(), name='user'),
	path('api-token-auth/', ObtainAuthToken.as_view()),
    path('authenticate/', 
         LoginAuthToken.as_view(), 
         name='authenticate'),

    path('ws/<int:cep>/', views.get_cep, name='get-cep')
]

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', 
         include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = helper_patterns
urlpatterns.extend(router.urls)
