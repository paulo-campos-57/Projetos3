from django.contrib.auth.models import User
from django.contrib.auth import get_user

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