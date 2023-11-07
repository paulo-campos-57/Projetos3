from django.shortcuts import render
from gestor.models import PerfilColaborador

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = PerfilColaborador.objects.get(user=request.user)
        except PerfilColaborador.DoesNotExist:
            perfil_colaborador = None
        
        return render(request, 'home.html', {'perfil_colaborador' : perfil_colaborador})

    else:
        return render(request, 'home.html')

def login(request):
    request.use=None
    return render(request, 'login.html')

def cadastro(request):
    request.use=None
    return render(request, 'cadastro.html')

def user_menu(request):
    return render(request, 'user.html')

def gestao_equipe(request):
    return render(request, 'gestao_equipe.html')