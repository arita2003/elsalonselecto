from django.shortcuts import render 
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from menu.models import Direccion
from .serializers import direccionSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import token

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])

def login (request):
    data = JASONPaser().parase(request)

    username = data['username']
    check_password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response ("usuario invalido")
    #validamos la contra
    pass_valido =check_password(password,user.password)
    if not pass_valido:
        return Response ("password incorrecta")
    #permitir o recuperar al token
    token, created = Token.objects.get_or_create(user.user)
    #print (token.key)
    return Response(token.key)    

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