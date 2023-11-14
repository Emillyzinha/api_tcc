from rest_framework import viewsets, status
from rest_framework.response import Response
from main.settings import BASE_DIR
from ..serializers.serializers import *
from ..IA.testesQA import *

callback_manager = callback_manager()

embeddings = HuggingFaceEmbeddings()

llm = return_llm(callback_manager, r"api/IA/modelo/llama-2-7b-chat.Q5_K_M.gguf")

vector_db = load_vector_db(str(BASE_DIR) + r'/api/IA/VECTOR_DB', embeddings)

template = template()

retriever = retriever(vector_db)


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
            if request.data["questao_1"][0] == "2":
                porcentagem_acertos = porcentagem_acertos + 0.25

            if request.data["questao_2"][0] == "1":
                porcentagem_acertos = porcentagem_acertos + 0.25

            if request.data["questao_3"][0] == "1":
                porcentagem_acertos = porcentagem_acertos + 0.25

            if request.data["questao_4"][0] == "2":
                porcentagem_acertos = porcentagem_acertos + 0.25

            return Response(int(porcentagem_acertos * 100), status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


class DocumentosViewset(viewsets.ModelViewSet):
    serializer_class = DocumentosSerializers
    queryset = Documentos.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            docs = preparing_documents(str(BASE_DIR) + r'/media/Documents')
            try:
                create_vector_db(docs, embeddings, str(BASE_DIR) + r'/api/IA/VECTOR_DB')
            except Exception:
                return Response("Não foi possível criar o(s) documento(s)", status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response("Adicione um documento", status.HTTP_400_BAD_REQUEST)


class ChatViewset(viewsets.ModelViewSet):
    serializer_class = ChatSerializers
    queryset = Chat.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(answer(llm, template, retriever, {"question": request.data["mensagem"]})["answer"], status.HTTP_201_CREATED)
            except Exception:
                return Response("Desculpe. Ocorreu um erro!", status.HTTP_400_BAD_REQUEST)
