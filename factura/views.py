from django.shortcuts import render
from rest_framework import generics
from factura.models import Productos, cliente, factura
from .serializers import ProductosSerializer,clienteSerializer, facturaSerializer

# Create your views here.
class ProductosListCreate(generics.ListCreateAPIView):
    queryset= Productos.objects.all()
    serializer_class=ProductosSerializer
    
class ProductosUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset= Productos.objects.all()
    serializer_class=ProductosSerializer
    
#Views for Clientes
class clienteListCreate(generics.ListCreateAPIView):
    queryset= cliente.objects.all()
    serializer_class=clienteSerializer
    
class ProductosUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset= cliente.objects.all()
    serializer_class=clienteSerializer

#Views for FACTURAS
class facturaListCreate(generics.ListCreateAPIView):
    queryset= cliente.objects.all()
    serializer_class=facturaSerializer
    
class facturaUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset= factura.objects.all()
    serializer_class=facturaSerializer