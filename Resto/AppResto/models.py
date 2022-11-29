from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.camada}'



class Plato(models.Model):
    
    plato =  models.CharField(max_length=50)
    guarnicion =  models.CharField(max_length=50) 
    precio =  models.IntegerField()

    def __str__(self):
        return f'{self.plato} - {self.guarnicion} - ${self.precio}'   


class Postre(models.Model):
    
    postre =  models.CharField(max_length=50)
    precio =  models.IntegerField()
  

    def __str__(self):
        return f'{self.postre} - ${self.precio}' 

class Bebida(models.Model):

    bebida =  models.CharField(max_length=50)
    precio =  models.IntegerField()
  

    def __str__(self):
        return f'{self.bebida} - ${self.precio}' 

