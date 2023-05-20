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