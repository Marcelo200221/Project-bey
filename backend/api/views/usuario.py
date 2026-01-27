from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, F
from django.db import IntegrityError
from rest_framework.views import APIView
from django.contrib.auth.models import User

@api_view(["GET"])
def cargar_usuarios(request):
    usuarios = User.objects.all()

    data = []
    for i in usuarios:
        list = {
            "id" : i.id,
            "nombre" : i.first_name + " " + i.last_name,
            "correo" : i.email,
            "username" : i.username
        }
        data.append(list)
    
    return Response(data)
