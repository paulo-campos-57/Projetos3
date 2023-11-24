from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
from gestor.models import PerfilColaborador, FormularioReporte, Mensagens
from gestor.DAOs.PerfilColaboradorDAO import intancePerfilColaborador, getPerfilColaborador, getFomulariosColaborador, getTodosPerfisColaborador
from .forms import PerfilColacoradorForm, FormularioReporteForm, MensagensForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = PerfilColaborador.objects.get(user=request.user)
        except PerfilColaborador.DoesNotExist:
            perfil_colaborador = None

    else:
        perfil_colaborador = None
    
    return render(request, 'index.html', {'perfil_colaborador' : perfil_colaborador})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Autentica o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Usuário autenticado com sucesso
            django_login(request, user)
            return redirect('home')
        else:
            # Falha na autenticação
            return render(request, 'login.html', {'error_message': 'Usuário não cadastrado!'})
    return render(request, 'login.html')

def cadastro(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid(): 
                user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            return('home.html')
        else:
            form = UserCreationForm()
        return render(request, 'cadastro.html', {'form': form})
    #request.use=None
    #return render(request, 'cadastro.html')

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

def homeMasterUser(request):
    return render(request, 'homeMasterUser.html')

def colaboradores(request):
    return render(request, 'colaboradores.html')

def enviar_mensagem(request):
    if request.method == 'POST':
        mensagens_form = MensagensForm(request.POST)

        if mensagens_form.is_valid():
            mensagem = mensagens_form.save(commit=False)
            if request.user.is_authenticated:
                mensagem.user = request.user
            else:
                return redirect("/login")
        mensagem.save()
    else:
        mensagens_form = MensagensForm()
        return redirect("/enviar_mensagem")

    return render(request, 'enviar_mensagem.html', 
                  {"mensagens_form": mensagens_form,})

def formulario_colaborador(request):
    perfil_colaborador = getPerfilColaborador(request)

    if request.method == 'POST':
        form = PerfilColacoradorForm(request.POST, instance=perfil_colaborador)

        if form.is_valid():
            user = request.user
            cargo = form.cleaned_data['cargo']
            motivacao = form.cleaned_data['motivacao']

            intancePerfilColaborador(user, cargo, motivacao, 'analise', False)

            return redirect("home")
        
    else:
        form = PerfilColacoradorForm(instance=perfil_colaborador)

    
    return render(request, 'formulario_colaborador.html', {'form': form})

def colaborador(request):
    perfil_colaborador = getPerfilColaborador(request)

    if perfil_colaborador == None or perfil_colaborador.atividade == False:
        return redirect("home")
    
    return render(request, 'colaborador.html', {'perfil_colaborador': perfil_colaborador})


def novos_membros(request):
    perfil_colaborador = getPerfilColaborador(request)

    if perfil_colaborador == None or perfil_colaborador.atividade == False:
        return redirect("home")
        
    return render(request, "add_gestores.html")

def novos_membros_formulario(request):
    perfil_colaborador = getPerfilColaborador(request)

    if perfil_colaborador == None or perfil_colaborador.atividade == False:
        return redirect("home")
    
    formularios = getFomulariosColaborador()
    
    return render(request, "add_gestores_formulario.html", {'perfil_colaborador' : perfil_colaborador, 'formularios' : formularios})

def novos_membros_buscar(request):
    perfil_colaborador = getPerfilColaborador(request)

    if perfil_colaborador == None or perfil_colaborador.atividade == False:
        return redirect("home")
    
    formularios = getFomulariosColaborador()
    
    return render(request, "add_gestores_buscar.html", {'perfil_colaborador' : perfil_colaborador, 'formularios' : formularios})
    
    

# def CriarFormularioMensagem(request):
    
    