import email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Productos(models.Model):
    producto = models.CharField(max_length=64)
    cantidad = models.IntegerField(null=True, blank=True)	
    precio = models.FloatField(null=True, blank=False)
    detalle= models.TextField(blank=True)

class cliente(models.Model):
    nombre_cliente = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    ciudad = models.CharField(max_length=64)
    telefono = models.IntegerField(null=True, blank=True)	
    email = models.EmailField( max_length=45)


class factura(models.Model):
    vendedor = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="vendedor")
    producto= models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
    nombre_cliente= models.ForeignKey(cliente, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=32)
    comentario = models.TextField(blank=True)
    creacion = models.DateField()
