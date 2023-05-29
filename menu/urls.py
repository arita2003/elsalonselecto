from django.contrib import admin
from django.urls import path,include
from .views import  index 
from . import views
urlpatterns = [
    path('', index, name="index"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('validacion_nuevo_usuario', views.validacion_nuevo_usuario, name='validacion_nuevo_usuario'),
    path('mi_formulario/', views.mi_formulario, name='mi_formulario'),
]