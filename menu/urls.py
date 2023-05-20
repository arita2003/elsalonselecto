from django.contrib import admin
from django.urls import path,incluide
from .views import entorno, index

urlpatterns = [
    path('', index, name="index"),
    path('entorno/', entorno, name="entorno"),
]