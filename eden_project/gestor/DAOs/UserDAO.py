from django.contrib.auth.models import User
from django.contrib.auth import get_user

def getUser(request):
    user = get_user(request)
    
    if request.user.is_authenticated:
        return user
    else:
        return None