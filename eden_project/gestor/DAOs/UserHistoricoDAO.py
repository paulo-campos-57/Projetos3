from gestor.models import UserHistorico

def getUserHistoricoByUser(user):
    try:
        historico = UserHistorico.objects.filter(user=user)
    except UserHistorico.DoesNotExist:
        historico = None

    return historico

def getTodosUserHistorico():
    try:
        historico = UserHistorico.objects.all()
    except UserHistorico.DoesNotExist:
        historico = None

    return historico

def getHistoricoComcluido(user):
    historico_filtrado = UserHistorico.objects.filter(user=user).filter(concluido=True)

    return historico_filtrado

def getHistoricoIncompletos(user):
    historico_filtrado = UserHistorico.objects.filter(user=user).filter(concluido=False)

    return historico_filtrado
