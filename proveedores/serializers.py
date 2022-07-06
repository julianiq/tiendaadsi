from rest_framework import serializers
from .models import proveedores

class proveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model= proveedores
        fields='__all__'