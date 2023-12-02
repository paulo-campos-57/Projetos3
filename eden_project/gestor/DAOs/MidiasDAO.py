from gestor.models import User, Midia
from gestor.DAOs.UserDAO import getUser


def instanceMidia(titulo, user, autor, descricao, status, dataPostagem, arqMidia, arqCartaz):
    midia, _ = Midia.objects.get_or_create(titulo=titulo)

    midia.titulo = titulo
    midia.user = user
    midia.autor = autor
    midia.descricao = descricao
    midia.status = status
    midia.dataPostagem = dataPostagem
    midia.arqMidia = arqMidia
    midia.arqCartaz = arqCartaz

    midia.save()

    return midia

def getMidiaByTitulo(titulo):
    try:
        midia = Midia.objects.get(titulo)
    except Midia.DoesNotExist:
        midia = None
    
    return midia

def getMidiaByAutor(autor):
    try:
        midia = Midia.objects.get(autor=autor)
    except Midia.DoesNotExist:
        midia = None

    return midia


def getTodasMidias():
    try:
        midias = Midia.objects.all()
    except Midia.DoesNotExist:
        midias = None
    
    return midias