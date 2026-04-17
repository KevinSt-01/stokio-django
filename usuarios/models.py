from django.db import models
#Para que herede de django y poder usar el authenticate y el hash de la password.
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.nombre


class Usuarios(AbstractUser): 
    correo = models.EmailField()
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null= True, blank=True)
  
    def __str__(self):
        return self.username
    
    class Meta: 
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'


#USER ADMIN: KevinSt -> 123Kevin
#USER NORMAL: Stiven Tabordad -> 123Stiven
