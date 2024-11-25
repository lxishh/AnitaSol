from django.db import models
from datetime import datetime

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=255)

class Propietaria(Usuario):
    pass

class Vendedora(Usuario):
    pass

class Inventario(models.Model):
    propietaria = models.OneToOneField(Propietaria, on_delete=models.CASCADE, primary_key=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    fecha_ingreso = models.DateField(default=datetime.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class InventarioProducto(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('inventario', 'producto')

class Venta(models.Model):
    fecha_ingreso = models.DateField()
    total = models.FloatField()

class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('venta', 'producto')
