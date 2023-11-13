import requests
from rest_framework import viewsets, status
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import action

from ..chatbot import chatbot
from ..models import Palavras, Resposta, Pergunta, Usuario, Treinamentos, Imagens, Questionario
from ..serializers.serializers import LuizaSerializer, RespostaSerializer, PerguntaSerializer, \
    UsuarioSerializer, TreinamentoSerializer, ImagensSerializer, QuestionarioSerializer

from rest_framework.permissions import IsAuthenticated




class LuizaViewset(viewsets.ModelViewSet):
    serializer_class = LuizaSerializer
    queryset = Palavras.objects.all()


class RespostaViewset(viewsets.ModelViewSet):
    serializer_class = RespostaSerializer
    queryset = Resposta.objects.all()


class PerguntaViewset(viewsets.ModelViewSet):
    serializer_class = PerguntaSerializer
    queryset = Pergunta.objects.all()


# class PerguntasFuturasViewset(viewsets.ModelViewSet):
#     serializer_class = PerguntasFuturasSerializer
#     queryset = Pergunta.objects.all()

class UsuarioViewset(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class TreinamentoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = TreinamentoSerializer
    queryset = Treinamentos.objects.all()


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImagensSerializer
    queryset = Imagens.objects.all()

class QuestionarioViewset(viewsets.ModelViewSet):
    serializer_class = QuestionarioSerializer
    queryset = Questionario.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        porcentagem_acertos = 0.0

        if serializer.is_valid():
            print(request.data)
            if request.data["questao_1"][0] == "2":
                porcentagem_acertos = porcentagem_acertos + 0.25

            if request.data["questao_2"][0] == "1":
                porcentagem_acertos = porcentagem_acertos + 0.25

            if request.data["questao_3"][0] == "1":
                porcentagem_acertos = porcentagem_acertos + 0.25

            if request.data["questao_4"][0] == "2":
                porcentagem_acertos = porcentagem_acertos + 0.25

            print(porcentagem_acertos)
            return Response(int(porcentagem_acertos * 100), status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status.HTTP_400_BAD_REQUEST)