from django.urls import path
from proveedores.models import proveedores

from proveedores.views import proveedoresListCreate, proveedoresUpdateDelete

urlpatterns =[
     path('proveedores/', proveedoresListCreate.as_view()),
     path('proveedores/<pk>/', proveedoresUpdateDelete.as_view())
    
]