from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def opciones(request):
    return render(request, 'opciones.html')