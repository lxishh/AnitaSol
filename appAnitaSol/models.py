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
        return self.nombre # Retorna el nombre de la categoría

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    fecha_ingreso = models.DateField(default=datetime.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre}"  # Muestra el nombre del producto y la categoría

class InventarioProducto(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('inventario', 'producto')

class Venta(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id}"


class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('venta', 'producto')

    def __str__(self):
        return f"{self.producto.nombre} en venta {self.venta.id} - Cantidad: {self.cantidad}"

