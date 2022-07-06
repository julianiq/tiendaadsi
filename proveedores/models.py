from django.db import models


# Create your models here.
class proveedores(models.Model):
    nombre_proveedor = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    ciudad = models.CharField(max_length=64)
    telefono = models.IntegerField(null=True, blank=True)	
    email = models.EmailField( max_length=45)