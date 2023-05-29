from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'menu/index.html')

def login(request):
    if request.method == 'POST':
        # Procesa los datos del formulario de inicio de sesión
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        # Procesa los datos del formulario de registro
        email = request.POST.get('email')
        
        
    return render(request, 'index.html')




def entorno(request):
    return render(request,'menu/entorno.html')

def recuperacion(request):
    return render(request,'menu/recuperacion.html')

def recuperacion2(request):
    return render(request,'menu/recuperacion2.html')

def recuperacion3(request):
    return render(request,'menu/recuperacion3.html')


def carrito(request):
    return render(request,'menu/carrito.html')

def form(request):
    return render(request,'menu/form.html')
def carrito(request):
    return render(request,'menu/carrito.html')

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


def mi_formulario(request):
    if request.method == 'POST':
        # Procesar los datos enviados por el formulario
        contraseña = request.POST.get('contraseña')
        confi_contraseña = request.POST.get('confi-contraseña')
        
        return render(request, 'crearnombre.html')
    else:
        return render(request, 'pas_nuevo_usuario.html')



def val_nuevo_usuario(request):
    return render(request,'menu/val_nuevo_usuario.html')



def validacion_nuevo_usuario(request):
    
    if request.method == 'POST':
        # Procesa los datos del formulario de validación de correo
        codigo_correo = request.POST.get('codigo_correo_nuevo_usuario')
        
        
        
    return render(request, 'val_nuevo_usuario.html')



def nosotros(request):
    return render(request,'menu/nosotros.html')

