from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, F
from django.db import IntegrityError
from rest_framework.views import APIView
from api.models import Chat, chatUsuario, Mensaje
from django.contrib.auth.models import User
from api.serializers import ChatDetalleSerializer


@api_view(["POST"])
def crear_chat(request):
    user = request.user

    if not user:
        return Response(
            {"error": "Usuario creador no existe"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    user_select = request.get.GET("id_usuario")

    try:
        user2 = User.objects.get(id=user_select)
    except User.DoesNotExist:
        return Response(
            {"error": "Usuario seleccionado no existe"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    nombre_chat = request.get.GET("nombre")
    
    if nombre_chat:
        Chat.objects.create(nombre = nombre_chat)
        chat = Chat.objects.get(nombre=nombre_chat)
    else:
        return Response(
            {"error": "No se recibió nombre de chat"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    chatUsuario.objects.create(id_usuario = user, id_chat = chat)
    chatUsuario.objects.create(id_usuario = user2, id_chat = chat)

    return Response(
        {"success": "Chat creado con exito"},
        status=status.HTTP_201_CREATED
    )

@api_view(["GET"])
def cargar_chat(request, pk):
    try:
        chat = Chat.objects.get(id=pk)
    except Chat.DoesNotExist:
        return Response(
            {"error": "El chat seleccionado no existe"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = ChatDetalleSerializer(chat)
    return Response(serializer.data, status = status.HTTP_200_OK)
    

    



