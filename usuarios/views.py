from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menuopciones')
         # Redirect to a success page.
        else:
            messages.success(request, 'Error al iniciar sesión, vuelva a intentarlo.')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')
    
def logout_usuario(request):
    logout(request)
    messages.success(request, 'Sesion cerrada con éxito')
    return redirect("home")

#create
def registrar_vendedor(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Crear usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # Agregar usuario al grupo "vendedores"
        group = Group.objects.get(name='vendedores')
        user.groups.add(group)

        return redirect('menuopciones')  # Redirige al menú de opciones

    return render(request, 'form_vendedores.html', {'action': 'Registrar'})


#read
def listar_vendedores(request):
    # Intentar obtener el grupo "vendedores"
    try:
        grupo = Group.objects.get(name='vendedores')
        usuarios = grupo.user_set.all()  # Obtiene solo los usuarios del grupo
    except Group.DoesNotExist:
        usuarios = User.objects.none()  # Retorna vacío si el grupo no existe

    # Pasar los usuarios al contexto
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'vendedores.html', context)

#update
def actualizar_vendedor(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('menuopciones')

    return render(request, 'form_vendedores.html', {'action': 'Actualizar', 'user': user})

#delete
def eliminar_vendedor(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('menuopciones')
