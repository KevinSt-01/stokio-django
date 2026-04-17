from django.db import models 

# Create your models here.
#1.Crear el modulo de producto. 

class Producto(models.Model): 
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_salida = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
#2.Despues registrar esta clase en el admin de la app productos. 