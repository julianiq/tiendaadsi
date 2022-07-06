from django.urls import path

from .views import ProductosUpdateDelete,facturaUpdateDelete, clienteUpdateDelete

from .views import ProductosListCreate, clienteListCreate, facturaListCreate

urlpatterns =[
    path('Productos/', ProductosListCreate.as_view()),
    path('clientes/',clienteListCreate.as_view()),
    path('facturas/',facturaListCreate.as_view()),
    path('Productos/<pk>/', ProductosUpdateDelete.as_view()),
    path('clientes/<pk>', clienteUpdateDelete),
    path('facturas/<pk>/', facturaUpdateDelete)
]