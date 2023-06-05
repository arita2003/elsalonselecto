from django.shortcuts import render 
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from menu.models import Direccion
from .serializers import direccionSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])

def datos_direccion(request):

    """
    TODOS LOS DATOS DE LA DIRECCION
    """

    if request.method == 'GET':
        
        direccion = Direccion.objects.all()
        serializer = direccionSerializer(direccion, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = direccionSerializer(data = data)

        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)