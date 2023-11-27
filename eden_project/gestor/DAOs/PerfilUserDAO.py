from gestor.models import PerfilUser
from gestor.DAOs.UserDAO import getUser, getUserNoColaboretors
import random

def intancePerfilUser(user):
    perfil, _ = PerfilUser.objects.get_or_create(user=user)

    foto = random.randint(1, 4)

    if foto == 1:
        perfil.foto = 'assets/fotos/foto1.jpeg'
    elif foto == 2:
        perfil.foto = 'assets/fotos/foto2.jpeg'
    elif foto == 3:
        perfil.foto = 'assets/fotos/foto3.jpeg'
    elif foto == 4:
        perfil.foto = 'assets/fotos/foto4.jpeg'

    perfil.save()

    return perfil

def getPerfilUser(request):
    user = getUser(request)

    try:
        perfil = PerfilUser.objects.get(user=user)
    except PerfilUser.DoesNotExist:
        perfil = None

    return perfil

def getPerfilUserByUser(users):   
    try:
        perfils = PerfilUser.objects.filter(user__in=users)
    except PerfilUser.DoesNotExist:
        perfils = None
        
    return perfils

def getPerfilUserColaboretors():
    users = getUserNoColaboretors()

    try:
        perfils = PerfilUser.objects.filter(user__in=users)
    except PerfilUser.DoesNotExist:
        perfils = None
        
    return perfils