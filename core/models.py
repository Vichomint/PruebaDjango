from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key = True,verbose_name = 'Id de categoria')
    nombreCategoria = models.CharField(max_length = 50, verbose_name = 'nombre de la categoria')
    def __str__(self):
        return self.nombreCategoria

class Estado(models.Model):
    idEstado = models.IntegerField(primary_key = True,verbose_name = 'Id de Estado')
    Estado = models.CharField(max_length = 20, verbose_name = 'Estado' )
    def __str__(self):
        return self.Estado


class Vehiculo(models.Model):
    patente = models.CharField(max_length = 6, primary_key= True, verbose_name = 'Patente')
    marca = models.CharField(max_length = 20, verbose_name = 'Marca Vehiculo')
    modelo = models.CharField(max_length = 20,null = True ,blank = True, verbose_name = 'Modelo')
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente


class Usuario(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True,verbose_name = 'nombre')
    email=models.CharField(max_length=300,verbose_name = 'email')
    password=models.CharField(max_length=10, verbose_name = 'password')


class fotosinfo(models.Model):
    imagen=models.CharField(max_length=100, default='')
    tipo = models.CharField(max_length=10,null = True, verbose_name='tipo')
    def __str__(self):
        return self.imagen   