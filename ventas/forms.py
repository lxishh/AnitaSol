from django import forms
from appAnitaSol.models import Producto, VentaProducto

class FormularioVenta(forms.Form):
    # Campo para seleccionar el producto
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), label="Producto", widget=forms.Select)
    
    # Campo para la cantidad
    cantidad = forms.IntegerField(min_value=1, label="Cantidad", widget=forms.NumberInput(attrs={'min': 1}))
