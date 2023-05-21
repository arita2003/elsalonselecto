from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'menu/index.html')

def entorno(request):
    return render(request,'menu/entorno.html')

def recuperacion(request):
    return render(request,'menu/recuperacion.html')

def recuperacion2(request):
    return render(request,'menu/recuperacion2.html')

def recuperacion3(request):
    return render(request,'menu/recuperacion3.html')

def entorno(request):
    return render(request,'menu/entorno.html')

def carrito(request):
    return render(request,'menu/carrito.html')

def form(request):
    return render(request,'menu/form.html')

def agregar_platillos(request):
    return render(request,'menu/agregar_platillos.html')

def platillos(request):
    return render(request,'menu/platillos.html')

def eliminar_platillos(request):
    return render(request,'menu/eliminar_platillos.html')

def perfil(request):
    return render(request,'menu/perfil.html')

def editar_perfil(request):
    return render(request,'menu/editar_perfil.html')

def pas_nuevo_usuario(request):
    return render(request,'menu/pas_nuevo_usuariohtml')

def val_nuevo_usuario(request):
    return render(request,'menu/val_nuevo_usuario.html')