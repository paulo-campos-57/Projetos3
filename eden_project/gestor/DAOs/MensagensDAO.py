from gestor.models import Mensagens

def intanceMensagemNotificacao(user, userDestino, mensagem):
    notificacao = Mensagens (
        user = user,
        userDestino = userDestino,
        mensagem = mensagem,
        contexto = 'notificacao'
    )

    notificacao.save()

def getNotificacaoUser(userDestino):
    notificacao = Mensagens.objects.filter(userDestino=userDestino)

    return notificacao