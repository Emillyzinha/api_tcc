from django.contrib.auth.hashers import make_password

from rest_framework import generics, status
from rest_framework.authtoken.admin import User
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import serializers
from .serializers.serializers import UsuarioSerializer
from .models import Usuario

import unidecode


class CadastroView(APIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if Usuario.objects.filter(email=request.data["email"]) or serializer.is_valid() is False:
            return Response("Houve um Problema!", status=status.HTTP_400_BAD_REQUEST)

        else:
            User.objects.create_user(username=request.data["email"], password=request.data["senha"],
                                     first_name=request.data["nome"], last_name=request.data["nome"])
            senha = make_password(request.data["senha"])
            serializer.is_valid()
            serializer.save(senha=senha)
            return Response("Usuário Criado Com Sucssso!", status=status.HTTP_201_CREATED)
