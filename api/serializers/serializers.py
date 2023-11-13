from rest_framework import serializers
from ..models import Palavras, Resposta, Pergunta, Usuario, Treinamentos, Imagens, Questionario


class LuizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palavras
        fields = '__all__'


class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'


class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = '__all__'


class CreateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ["pergunta"]


# class PerguntasFuturasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PerguntasFuturas
#         fields = '__all__'

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
