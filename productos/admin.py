from django.contrib import admin

#3. importar desde models, se pone el . porque estamos dentro de la carpeta de productos.
from .models import Producto
# Register your models here.
#Esta clase se crea para ver cuales campos quiero ver ademas del nombre.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("id","nombre", "categoria","precio", "stock","descripcion","fecha_ingreso","fecha_salida")
    search_fields = ("nombre","categoria","precio","fecha_ingreso","fecha_salida")
    list_filter = ("nombre","categoria","fecha_ingreso","fecha_salida")
#4. Registrar el modelo de models. 
admin.site.register(Producto, ProductosAdmin)
#5. Crear un superusuario en la terminal.
#Usuario: KevinSt - Pass: 1913Lmdi