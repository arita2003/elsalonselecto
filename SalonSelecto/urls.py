"""SalonSelecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from menu.views import recuperacion, recuperacion2, recuperacion3,entorno,carrito,form,agregar_platillos, platillos,eliminar_platillos,perfil,editar_perfil, pas_nuevo_usuario,val_nuevo_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('recuperacion.html', recuperacion, name="recuperacion"),
    path('recuperacion2.html', recuperacion2, name="recuperacion2"),
    path('recuperacion3.html', recuperacion3, name="recuperacion3"),
    path('entorno.html', entorno, name="entorno"),
    path('carrito.html', carrito, name="carrito"),
    path('form.html', form, name="form"),
    path('agregar_platillos', agregar_platillos, name="agregar_platillos"),
    path(' platillos',  platillos, name=" platillos"),
    path('eliminar_platillos',eliminar_platillos, name="eliminar_platillos"),
    path('perfil',perfil, name="perfil"),
    path('editar_perfil', editar_perfil, name="editar_perfil"),
    path('pas_nuevo_usuario', pas_nuevo_usuario, name="pas_nuevo_usuario"),
    path('val_nuevo_usuario', val_nuevo_usuario, name="val_nuevo_usuario")
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




