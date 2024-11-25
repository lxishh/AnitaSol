from django.urls import path
from . import views

urlpatterns = [
    path('read_productos', views.login_usuario, name='login'),
]