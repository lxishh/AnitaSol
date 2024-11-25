from django.shortcuts import render, redirect
from ventas.forms import FormularioVenta
from appAnitaSol.models import Venta, Producto, VentaProducto

# Create
def registrar_venta(request):
    total = 0.0
    if request.method == 'POST':
        form = FormularioVenta(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']
            
            # Crear una nueva venta
            venta = Venta.objects.create(total=0)  # Inicializamos con total = 0

            # Crear la relación VentaProducto
            venta_producto = VentaProducto.objects.create(venta=venta, producto=producto, cantidad=cantidad)
            
            # Calcular el total de la venta
            total = venta_producto.producto.precio * venta_producto.cantidad

            # Actualizar el total de la venta
            venta.total = total
            venta.save()

            return redirect('ventas')  # Redirige a la vista de listar ventas
    else:
        form = FormularioVenta()

    return render(request, 'form_venta.html', {'form': form, 'total': total})

# Read
def listar_ventas(request):
    ventas = Venta.objects.all()  # Obtiene todas las ventas registradas
    context = {'ventas': ventas}
    return render(request, 'ventas.html', context)  # Renderiza las ventas en la plantilla

def actualizar_venta(request, id):
    venta = Venta.objects.get(id=id)  # Obtiene la venta por ID
    venta_productos = VentaProducto.objects.filter(venta=venta)  # Obtiene los productos asociados a la venta

    if request.method == 'POST':
        # Actualizar productos y cantidades en la venta
        for vp in venta_productos:
            producto_id = request.POST.get(f'producto_{vp.producto.id}')
            cantidad = int(request.POST.get(f'cantidad_{vp.producto.id}'))
            
            # Verifica que se haya enviado un nuevo producto (en caso de querer cambiarlo)
            if producto_id:
                producto = Producto.objects.get(id=producto_id)
                vp.producto = producto
            vp.cantidad = cantidad
            vp.save()

        # Recalcular el total de la venta
        total = sum(vp.producto.precio * vp.cantidad for vp in venta_productos)
        venta.total = total
        venta.save()

        return redirect('ventas')  # Redirige a la vista de listar ventas

    # Si no es POST, mostramos el formulario con los productos de la venta
    context = {
        'venta': venta,
        'venta_productos': venta_productos,  # Los productos de la venta que se deben editar
        'productos': Producto.objects.all(),  # Todos los productos disponibles para selección
    }

    return render(request, 'form_edit_venta.html', context)  # Muestra el formulario para editar la venta



# Delete
def eliminar_venta(request, id):
    venta = Venta.objects.get(id=id)  # Obtiene la venta por ID
    
    # Elimina los productos asociados a la venta
    VentaProducto.objects.filter(venta=venta).delete()
    
    # Elimina la venta
    venta.delete()
    return redirect('ventas')  # Redirige a la vista de listar ventas
