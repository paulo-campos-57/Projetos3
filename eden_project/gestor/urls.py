from django.urls import path
from gestor.views import home, login, cadastro, user_menu, gestao_equipe, colaboradores, usuario_cadastrado, testegestao, enviar_mensagem


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('login/cadastro', cadastro, name='cadastro'),
    path('cadastro/efetuado', usuario_cadastrado, name='usuario_cadastrado'),
    path('user/', user_menu, name='user_menu'),
    path('gestao_equipe/', gestao_equipe, name='gestao_equipe'),
    path('teste_gestao/', testegestao, name='testegestao'),
    path('colaboradores/', colaboradores, name='colaboradores'),
    path('enviar_mensagem/', enviar_mensagem, name='enviar_mensagem'),
]