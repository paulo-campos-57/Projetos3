from django.shortcuts import render

# Create your views here.

def home(request):
    request.use=None
    return render(request, 'home.html')

def login(request):
    request.use=None
    return render(request, 'login.html')

def cadastro(request):
    request.use=None
    return render(request, 'cadastro.html')

def user_menu(request):
    return render(request, 'user.html')