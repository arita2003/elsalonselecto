from rest_framework import serializers
from menu.models import Direccion

class direccionSerializer(serializers.ModelSerializer):
    class meta:
        model = Direccion
        fields = ['id_direccion','calle', 'numero', 'codigo_postal', 'comuna']