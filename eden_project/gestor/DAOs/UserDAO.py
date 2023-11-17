from django.contrib.auth.models import User
from django.contrib.auth import get_user

def getUser():
    user = get_user()
    
    if user.is_authenticade:
        return user
    else:
        return None