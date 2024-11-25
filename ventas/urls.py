from django.urls import path
from . import views

urlpatterns = [
    path('listado/', views.listar_ventas, name='ventas'),
    path('registrar/', views.registrar_venta, name='registrarventa'),
    path('actualizar/<int:id>', views.actualizar_venta, name='actualizarventa'),
    path('eliminar/<int:id>', views.eliminar_venta, name='eliminarventa'),
]