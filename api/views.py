from django.contrib.auth.hashers import make_password

from rest_framework import generics, status
from rest_framework.authtoken.admin import User
from rest_framework.views import APIView
from rest_framework.response import Response

from .chatbot.chatbot import ChatBot, get_response
from .serializers import serializers
from .serializers.serializers import UsuarioSerializer
from .models import Pergunta, Resposta, Usuario

import unidecode


class PerguntaView(generics.ListAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = serializers.PerguntaSerializer


class CreateResponseView(APIView):
    serializer_class = serializers.CreateResponseSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.is_valid(raise_exception=True)
            serializer.save()
            pergunta = serializer.data['pergunta']
            pergunta = unidecode.unidecode(pergunta)
            chatbot = ChatBot()
            json = chatbot.get_json("http://127.0.0.1:8000/json/")
            ints = chatbot.predict_class(pergunta)
            try:
                get_response(ints, json)
            except (ValueError, IndexError, KeyError):
                return Response("Desculpe não entendi sua pergunta.", status=status.HTTP_400_BAD_REQUEST)
            else:
                dados = Resposta.objects.values()
                for i in range(len(dados)):
                    if i == len(dados) - 1:
                        return Response(dados[i]["resposta"], status=status.HTTP_201_CREATED)


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
