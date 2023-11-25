from django.urls import path
from gestor.views import home, login, logout_logic, cadastro, user_menu, gestao_equipe, colaboradores, usuario_cadastrado, homeMasterUser, enviar_mensagem, formulario_colaborador, colaborador, novos_membros, novos_membros_formulario, novos_membros_buscar


urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('login/cadastro', cadastro, name='cadastro'),
    path('logout', logout_logic, name='logout'),
    path('cadastro/efetuado', usuario_cadastrado, name='usuario_cadastrado'),
    path('user', user_menu, name='user_menu'),
    path('gestao_equipe', gestao_equipe, name='gestao_equipe'),
    path('colaboradores', colaboradores, name='colaboradores'),
    path('enviar_mensagem', enviar_mensagem, name='enviar_mensagem'),
    path('formulario_colaborador', formulario_colaborador, name='formulario_colaborador'),
    path('colaborador', colaborador, name='colaborador'),
    path('home', homeMasterUser, name='homeMasterUser'),
    path('novos_membros', novos_membros, name='novos_membros'),
    path('novos_membros/formulario', novos_membros_formulario, name='novos_membros_formulario'),
    path('novos_membros/buscar', novos_membros_buscar, name='novos_membros_buscar')
]