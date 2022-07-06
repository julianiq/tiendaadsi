from django.contrib import admin
from .models import cliente, Productos, factura

# Register your models here.


admin.site.register(cliente)
admin.site.register(Productos)
admin.site.register(factura)