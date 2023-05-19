from django.contrib import admin
from django.urls import path, include
from .views import entorno, index

urlpatterns = [
    path('',index,name="index"),
    path('entorno/',entorno,name="entorno"),
]
if setings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)