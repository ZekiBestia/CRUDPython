from django.db import models

# Create your models here.
class Pan(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripcion",null=True)

    def __str__(self):
        fila = self.nombre +" - " + "Stock: " + str(self.stock)
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    sueldo = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)

    def __str__(self):
        fila = self.nombre +" - " + self.apellido+" - " + self.ocupacion
        return fila
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
