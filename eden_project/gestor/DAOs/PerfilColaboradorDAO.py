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

def getFomulariosColaborador():   
    try:
        perfils = PerfilColaborador.objects.filter(status= 'analise')
    except PerfilColaborador.DoesNotExist:
        perfils = None
        
    return perfils


def getTodosPerfisColaborador():
    try:
        perfils = PerfilColaborador.objects.filter(atividade=True)
    except PerfilColaborador.DoesNotExist:
        perfils = None

    return perfils

