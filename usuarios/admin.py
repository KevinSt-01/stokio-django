from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios,Rol

admin.site.register(Rol)
@admin.register(Usuarios)
class UsuariosAdmin(UserAdmin): 
    list_display = ('username', 'email', 'correo','rol', 'is_staff', 'is_superuser','password')
    search_fields = ('username', 'email','correo')


