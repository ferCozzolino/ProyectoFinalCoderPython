from django.db import models


# Create your models here.

class PlatoPrincipal(models.Model):

    combo = models.IntegerField()
    plato =  models.CharField(max_length=50)
    guarnicion =  models.CharField(max_length=50) 
    precio =  models.IntegerField()

    def __str__(self):
        return f'{self.combo} - {self.plato} - {self.guarnicion} - ${self.precio}'   


class Postre(models.Model):

    codPostre = models.IntegerField()
    postre =  models.CharField(max_length=50)
    precio =  models.IntegerField()
  

    def __str__(self):
        return f'{self.codPostre} - {self.postre} - ${self.precio}' 

class Bebida(models.Model):

    codBebida = models.IntegerField()
    bebida =  models.CharField(max_length=50)
    precio =  models.IntegerField()
  

    def __str__(self):
        return f'{self.codBebida} - {self.bebida} - ${self.precio}' 



        