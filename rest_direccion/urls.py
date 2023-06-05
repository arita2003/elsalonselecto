from django.urls import path
from rest_direccion.views import datos_direccion

urlpatterns = [
    path('datos_direccion/', datos_direccion, name = "datos_direccion")
]