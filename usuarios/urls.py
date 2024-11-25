from django.urls import path
from . import views

urlpatterns = [
    path('login_usuario', views.login_usuario, name='login'),
    path('logout_usuario', views.logout_usuario, name='logout'),
    path('vendedores/', views.listar_vendedores, name='vendedores'),
    path('registrar_vendedor/', views.registrar_vendedor, name='registrarvendedor'),
    path('actualizar/<int:id>', views.actualizar_vendedor, name='actualizarvendedor'),
    path('eliminar/<int:id>', views.eliminar_vendedor, name='eliminarvendedor'),
]