from gestor.models import User, PerfilColaborador
from gestor.DAOs.UserDAO import getUser

def intancePerfilColaborador(user, cargo, motivacao, status, atividade):
    perfil, _ = PerfilColaborador.objects.get_or_create(user=user)

    perfil.cargo = cargo
    perfil.motivacao = motivacao
    perfil.status = status
    perfil.atividade = atividade

    perfil.save()

    return perfil

def getPerfilColaborador(request):
    user = getUser(request)

    try:
        perfil = PerfilColaborador.objects.get(user=user)
    except PerfilColaborador.DoesNotExist:
        perfil = None

    return perfil

def setPerfilColaboradorAtividade(user, atividade):
    perfil, _ = PerfilColaborador.objects.get_or_create(user=user)

    perfil.atividade = atividade
    perfil.save()


def setPerfilColaboradorStatus(user, status):
    perfil, _ = PerfilColaborador.objects.get_or_create(user=user)

    perfil.status = status
    perfil.save()


def getPerfilColaboradorByUser(user):
    try:
        perfil = PerfilColaborador.objects.get(user=user)
    except PerfilColaborador.DoesNotExist:
        perfil = None

    return perfil

def getFomulariosColaborador():   
    try:
        perfils = PerfilColaborador.objects.filter(status= 'analise').filter(atividade=False)
    except PerfilColaborador.DoesNotExist:
        perfils = None
        
    return perfils


def getTodosPerfisColaborador():
    try:
        perfils = PerfilColaborador.objects.filter(atividade=True)
    except PerfilColaborador.DoesNotExist:
        perfils = None

    return perfils

