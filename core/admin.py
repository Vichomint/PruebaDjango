from django.contrib import admin
from .models import Categoria, Vehiculo,Usuario,fotosinfo,Estado

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(Usuario)
admin.site.register(fotosinfo)
admin.site.register(Estado)

