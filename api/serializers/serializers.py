from rest_framework import serializers
from ..models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class TreinamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamentos
        fields = "__all__"


class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = "__all__"


class QuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionario
        fields = "__all__"


class DocumentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = "__all__"


class ChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
