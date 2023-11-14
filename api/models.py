import uuid

from .choices import QUESTION_1_CHOICES, QUESTION_2_CHOICES, QUESTION_3_CHOICES, QUESTION_4_CHOICES, QUESTION_5_CHOICES

from django.db import models
from django.db.models import UUIDField


class Usuario(models.Model):
    objects = None
    id_usuario = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    senha = models.TextField(max_length=100, editable=True, default=uuid.uuid4)
    nome = models.TextField(max_length=100, editable=True)
    email = models.EmailField()

    def __str__(self):
        return str(self.id_usuario)


class Treinamentos(models.Model):
    objects = None
    id_curso = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    imagem = models.FileField(upload_to="media", blank=True)
    nome = models.CharField(max_length=100, editable=True)
    descricao = models.CharField(max_length=350, editable=True)

    def __str__(self) -> str:
        return str(self.id_curso)


class Imagens(models.Model):
    id_imagem = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    id_treinamento = models.ForeignKey(Treinamentos, on_delete=models.CASCADE)
    imagem = models.FileField(upload_to="media")

    def __str__(self) -> str:
        return str(self.id_imagem)


class Questionario(models.Model):
    id_questionario = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    id_usuario = models.EmailField()
    questao_1 = models.CharField(max_length=1, choices=QUESTION_1_CHOICES, editable=True)
    questao_2 = models.CharField(max_length=1, choices=QUESTION_2_CHOICES, editable=True)
    questao_3 = models.CharField(max_length=1, choices=QUESTION_3_CHOICES, editable=True)
    questao_4 = models.CharField(max_length=1, choices=QUESTION_4_CHOICES, editable=True)
    questao_5 = models.CharField(max_length=1, choices=QUESTION_5_CHOICES, editable=True)


class Documentos(models.Model):
    id_documento = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    documento = models.FileField(upload_to="Documents", unique=True)


class Chat(models.Model):
    id_mensagem = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    mensagem = models.CharField(max_length=1000,editable=True)
