from django.contrib import admin
from .models import Articulo, Empleado, Lavado, LavadoHasArticulo, LugarCompra, Paquete, RolEmpleado
# Register your models here.
admin.site.register(Empleado)
admin.site.register(RolEmpleado)
admin.site.register(Paquete)
admin.site.register(LugarCompra)
admin.site.register(LavadoHasArticulo)
admin.site.register(Articulo)
