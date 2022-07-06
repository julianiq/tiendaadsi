from django.shortcuts import render
from rest_framework import generics
from proveedores.models import proveedores
from .serializers import proveedoresSerializer

# Create your views here.
class proveedoresSoporteListCreate(generics.ListCreateAPIView):
    queryset= proveedores.objects.all()
    serializer_class=proveedoresSerializer
    
class proveedoresUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset= proveedores.objects.all()
    serializer_class=proveedoresSerializer