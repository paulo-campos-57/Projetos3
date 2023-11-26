from gestor.models import User
from django.contrib.auth import get_user
from django.db.models import Q

def getUser(request):
    user = get_user(request)
    
    if request.user.is_authenticated:
        return user
    else:
        return None

def instanceUser(username, password, email):
        user = User.objects.create_user(username=username, password=password, email=email)
        return user

def getUserByUsername(username):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None
        
def getUserById(id):
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            return None
        
def getUserNoColaboretors():
        try:
            user = User.objects.filter(Q(perfilcolaborador__isnull=True) | Q(perfilcolaborador__atividade=False))
            return user
        except User.DoesNotExist:
            return None