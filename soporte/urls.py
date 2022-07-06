from django.urls import path

from soporte.views import PersonaSoporteListCreate, PersonaSoporteUpdateDelete

urlpatterns =[
     path('persona-soporte/', PersonaSoporteListCreate.as_view()),
     path('persona-soporte/<pk>/',PersonaSoporteUpdateDelete.as_view())
]