from django.contrib import admin
from django.urls import path,include
from .views import entorno, index, recuperacion, recuperacion2, recuperacion3

urlpatterns = [
    path('', index, name="index"),
    path('entorno/', entorno, name="entorno"),
    path('recuperacion/', recuperacion, name="recuperacion"),
    path('recuperacion2/', recuperacion2, name="recuperacion2"),
    path('recuperacion3/', recuperacion3, name="recuperacion3")
]