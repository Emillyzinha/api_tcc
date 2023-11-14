"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from api.viewsets import viewsets
from api.views import CadastroView
from rest_framework_simplejwt import views as jwt_views

from main import settings

route = routers.DefaultRouter()


# route.register(r'perguntas_futuras',viewsets.PerguntasFuturasViewset, basename='perguntas_futuras')
# route.register(r'cadastro',viewsets.UsuarioViewset, basename='cadastro')
route.register(r'treinamento', viewsets.TreinamentoViewSet, basename='treinamento')
route.register(r'imagens', viewsets.ImageViewSet, basename='imagens')
route.register(r'questionario', viewsets.QuestionarioViewset, basename='questionario')
route.register(r'documentos', viewsets.DocumentosViewset, basename="documentos")
route.register(r'chat', viewsets.ChatViewset, basename="chat")

urlpatterns = [
    path('', include(route.urls)),
    path('admin/', admin.site.urls),
    path('cadastro/', CadastroView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
