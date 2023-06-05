from rest_framework import serializers
from menu.models import Direccion

class direccionSerializer(serializers.ModelSerializer):
    class meta:
        model = Direccion
        fields = ['calle', 'comuna', 'numero', 'codigo_postal']