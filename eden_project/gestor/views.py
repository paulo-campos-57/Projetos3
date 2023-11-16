from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
from gestor.models import PerfilColaborador, FormularioReporte, Mensagens
from .forms import FormularioReporteForm, MensagensForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = PerfilColaborador.objects.get(user=request.user)
        except PerfilColaborador.DoesNotExist:
            perfil_colaborador = None

    else:
        perfil_colaborador = None
    
    return render(request, 'home.html', {'perfil_colaborador' : perfil_colaborador})

def login(request):
    request.use=None
    return render(request, 'login.html')

def cadastro(request):
    request.use=None
    return render(request, 'cadastro.html')

def usuario_cadastrado(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Verificar se o usuário já existe no banco de dados
        if User.objects.filter(username = username).exists():
            return HttpResponse('Este usuário já está cadastrado em nosso Banco de dados')
        user = User.objects.create_user(username, email, password)
        return render(request, 'usuario_cadastrado.html')

def user_menu(request):
    return render(request, 'user.html')

def gestao_equipe(request):
    return render(request, 'gestao_equipe.html')

def testegestao(request):
    return render(request, 'testegestao.html')

def colaboradores(request):
    return render(request, 'colaboradores.html')

def enviar_mensagem(request):
    if request.method == 'POST':
        mensagens_form = MensagensForm(request.POST)

        if mensagens_form.is_valid():
            mensagens_form.save()
            return redirect("/enviar_mensagem")
    else:
        mensagens_form = MensagensForm()

    return render(request, 'enviar_mensagem.html', {"mensagens_form": mensagens_form,})