from django.db import models

# Create your models here.

class Estadios(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    num_camerinos = models.IntegerField()
    num_marcadores = models.IntegerField()
    num_cabinas_radio = models.IntegerField()
    direccion = models.CharField(max_length=50)
    
    
    def __str__(self):
        return "%s %s %s %s %s %s" % (self.nombre, self.capacidad, self.num_camerinos, self.num_marcadores, \
            self.num_cabinas_radio, self.direccion)
        
        
        
class Parques(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    num_monumentos = models.IntegerField()
    
    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.direccion, self.tipo, self.num_monumentos)