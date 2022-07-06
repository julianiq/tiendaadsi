from rest_framework import serializers
from .models import cliente, Productos, factura

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= cliente
        fields='__all__'
        
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productos
        fields='__all__'

class facturaSerializer(serializers.ModelSerializer):
    class Meta:
        model= factura
        fields='__all__'