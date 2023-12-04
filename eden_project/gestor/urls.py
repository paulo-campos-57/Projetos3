from django.urls import path
from gestor.views import home, login, logout_logic, cadastro, user_menu, gestao_equipe, colaboradores, usuario_cadastrado, homeMasterUser, enviar_mensagem, formulario_colaborador, novos_membros, novos_membros_formulario, novos_membros_buscar, novos_membros_buscar_user, gestao_equipe_buscar_user, novos_membros_formulario_user, suporte_e_reporte, configuracoes, gestao_titulos, aceitar_chamar, negar_chamar, formulario_suporte,enviar_formulario_suporte, execluir_notificacao,remocao_midia
from .views import remocao, alterar_cargo

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
    path('home', homeMasterUser, name='homeMasterUser'),
    path('novos_membros', novos_membros, name='novos_membros'),
    path('novos_membros/formulario', novos_membros_formulario, name='novos_membros_formulario'),
    path('novos_membros/buscar', novos_membros_buscar, name='novos_membros_buscar'),
    path('novos_membros/buscar/usuario/<int:user_id>', novos_membros_buscar_user, name='novos_membros_buscar_user'),
    path('gestao_equipe/buscar/usuario/<int:user_id>', gestao_equipe_buscar_user, name='gestao_equipe_buscar_user'),
    path('novos_membros/formulario/usuario/<int:user_id>', novos_membros_formulario_user, name='novos_membros_formulario_user'),
    path('remover_usuario/<int:perfil_id>/', remocao, name='remover_usuario'),
    path('suporte_e_reporte', suporte_e_reporte, name='suporte_e_reporte'),
    path('configuracoes', configuracoes, name='configuracoes'),
    path('gestao_titulos', gestao_titulos, name='gestao_titulos'),
    # pode ser q aqui tenha alguma coisinha calmae
    
    path('alterar_cargo/<int:perfil_id>/', alterar_cargo, name='alterar_cargo'),
    path('noficicacao/chamar_equipe/aceitar', aceitar_chamar, name='aceitar_chamar'),
    path('noficicacao/chamar_equipe/negar', negar_chamar, name='negar_chamar'),
    path('formulario_suporte', formulario_suporte, name='formulario_suporte'),
    path('enviar-formulario-suporte/', enviar_formulario_suporte, name='enviar_formulario_suporte'),
    path('notificacao/excluir', execluir_notificacao, name='execluir_notificacao'),
    path('remocao_midia/<int:midia_id>', remocao_midia, name='remocao_midia'),]    
