from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from gestor.models import User, PerfilColaborador, FormularioReporte, Mensagens
from gestor.DAOs.PerfilColaboradorDAO import intancePerfilColaborador, getPerfilColaborador, getFomulariosColaborador, getTodosPerfisColaborador
from gestor.DAOs.UserDAO import getUserNoColaboretors, getUserById
from .forms import PerfilColacoradorForm, FormularioReporteForm, MensagensForm
from django.contrib.auth import authenticate, logout, login as django_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = PerfilColaborador.objects.get(user=request.user)
        except PerfilColaborador.DoesNotExist:
            perfil_colaborador = None

    else:
        return redirect("login")
    
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

def logout_logic(request):
    logout(request)

    return redirect("login")

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
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
        
    else:
        return redirect("login")
    
    return render(request, 'gestao_equipe.html', {'perfil_colaborador' : perfil_colaborador})

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

def novos_membros(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
        
    else:
        return redirect("login")

        
    return render(request, "add_gestores.html", {'perfil_colaborador' : perfil_colaborador})

def novos_membros_formulario(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
        
    else:
        return redirect("login")
    
    formularios = getFomulariosColaborador()
    
    return render(request, "add_gestores_formulario.html", {'perfil_colaborador' : perfil_colaborador, 'formularios' : formularios})

def novos_membros_buscar(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
        
    else:
        return redirect("login")
    
    users_no_colaborator = getUserNoColaboretors()

    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        users = [
            user for user in users_no_colaborator
            if search_query.lower() in user.username.lower() or search_query.lower() in user.email.lower()
        ]
        
        user_list = [{'username': user.username, 'last_login': user.last_login, 'email': user.email} for user in users]
        return JsonResponse({'users': user_list})
    
    return render(request, "add_gestores_buscar.html", {'perfil_colaborador' : perfil_colaborador, 'users_no_colaborator' : users_no_colaborator})
    
def novos_membros_buscar_user(request, user_id):
    user = getUserById(user_id)

    return render(request, 'add_gestores_buscar_user.html', {'user': user})
    

# def CriarFormularioMensagem(request):
    
    