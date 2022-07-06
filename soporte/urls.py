from django.urls import path
from soporte.models import PQR

from soporte.views import PQRListCreate, PQRUpdateDelete, PersonaSoporteListCreate, PersonaSoporteUpdateDelete

urlpatterns =[
     path('persona-soporte/', PersonaSoporteListCreate.as_view()),
     path('persona-soporte/<pk>/',PersonaSoporteUpdateDelete.as_view()),
     path('PQR/', PQRListCreate.as_view()),
     path('PQR/<pk>/',PQRUpdateDelete.as_view())
     
]