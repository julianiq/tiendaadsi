from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PersonaSoporte(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="soporte")
    nombre = models.CharField(max_length=64)
    edad = models.IntegerField(null=True, blank=True)	
    activo = models.BooleanField(default=True)

class PQR(models.Model):
    persona_soporte = models.ForeignKey(PersonaSoporte, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=32)
    comentario = models.TextField(blank=True)
    creacion = models.DateField()	



