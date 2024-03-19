from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    
# Metadatos - es info que nos sirve para interpretar
# Definimos Metadatos
class Meta:
    # orden descendente, por nombre
    ordering = ['-nombre']
    
# Definimos Metodos 
def __str__(self):
    return self.nombre

def get_absolute_url(self):
    pass
