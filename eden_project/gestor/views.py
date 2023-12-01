from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from gestor.models import PerfilColaborador, FormularioSuporte, FormularioReporte, Mensagens
from gestor.DAOs.PerfilColaboradorDAO import intancePerfilColaborador, setPerfilColaboradorAtividade, setPerfilColaboradorStatus, getPerfilColaborador, getFomulariosColaborador, getTodosPerfisColaborador, getPerfilColaboradorByUser
from gestor.DAOs.UserDAO import getUser, getUserNoColaboretors, getUserById
from gestor.DAOs.UserHistoricoDAO import getHistoricoComcluido, getHistoricoIncompletos
from gestor.DAOs.UserFeedbackDAO import getFeedbacksUser
from gestor.DAOs.FormularioReporteDAO import getFormularioReporteUser
from gestor.DAOs.FormularioSuporteDAO import getFormularioSuporteUser
from .forms import PerfilColacoradorForm, FormularioReporteForm, MensagensForm, PerfilColacoradorFormChamar, FormularioVazio
from django.contrib.auth import authenticate, logout, login as django_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
import logging
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            perfil_colaborador = None

    else:
        return redirect("login")
    
    return render(request, 'index.html', {'perfil_colaborador' : perfil_colaborador})

def aceitar_chamar(request):
    user = getUser(request)

    setPerfilColaboradorStatus(user, 'aprovado')
    return redirect("home")


def negar_chamar(request):
    perfil_colaborador = getPerfilColaborador(request)

    perfil_colaborador.delete()
    return redirect("home")

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
    
    perfis_colaboradores = getTodosPerfisColaborador()
    users = []

    if 'search_query' in request.GET:
        search_query = request.GET['search_query'].lower()
        for perfil in perfis_colaboradores:
            if search_query in perfil.user.username.lower() or search_query in perfil.user.email.lower():
                users.append({
                    'username': perfil.user.username,
                    'cargo': perfil.cargo,
                    'email': perfil.user.email,
                    'last_login': perfil.user.last_login
                })

        return JsonResponse({'users': users})
    
    return render(request, "gestao_equipe.html", {'perfil_colaborador': perfil_colaborador, 'perfis_colaboradores': perfis_colaboradores})

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
    user = getUser(request)

    if perfil_colaborador == None:
        perfil_colaborador = intancePerfilColaborador(user, 'null', " ", 'preenchendo', False)
    elif perfil_colaborador == 'aprovado' or perfil_colaborador == 'analise':
        return redirect("home")

    if request.method == 'POST':
        submit_type = request.POST.get('submit_type')

        if submit_type == 'enviar':
            form = PerfilColacoradorForm(request.POST, instance=perfil_colaborador)

            if form.is_valid():
                form.save()

                cargo = request.POST.get('cargo')
                motivacao = request.POST.get('motivacao')
                intancePerfilColaborador(user, cargo, motivacao, 'analise', False)

                return redirect("home")
        
        elif submit_type == 'descartar':
            perfil_colaborador.delete()
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
            if (
                search_query.lower() in user.username.lower()
                or search_query.lower() in user.email.lower()
                or search_query.lower() in user.first_name.lower()
                or search_query.lower() in user.last_name.lower()
            )
        ]


        user_list = [{'first_name': user.first_name, 'last_name': user.last_name, 'username': user.username, 'last_login': user.last_login, 'email': user.email} for user in users]
        return JsonResponse({'users': user_list})

    return render(request, "add_gestores_buscar.html", {'perfil_colaborador' : perfil_colaborador, 'users_no_colaborator' : users_no_colaborator})
    
def novos_membros_buscar_user(request, user_id):
    user_ = getUserById(user_id)

    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
    else:
        return redirect("login")
    
    feedback_user = getFeedbacksUser(user_)
    reporte_user = getFormularioReporteUser(user_)
    suporte_user = getFormularioSuporteUser(user_)

    dados_interacoes = {
        'numero1' : int(feedback_user.count()),
        'numero2' : int (reporte_user.count() + suporte_user.count()),
    }
    
    historico_concluido = getHistoricoComcluido(user_)
    historico_incompleto = getHistoricoIncompletos(user_)

    dados_histrico = {
        'numero1' : int(historico_concluido.count()),
        'numero2' : int(historico_incompleto.count()),
    }

    perfil_colaborador_user = getPerfilColaboradorByUser(user_)

    if perfil_colaborador_user == None:
        perfil_colaborador_user = intancePerfilColaborador(user_, 'null', " ", 'preenchendo', False)

    if request.method == 'POST':
        form = PerfilColacoradorFormChamar(request.POST)

        if form.is_valid():
            perfil_colaborador = form.save(commit=False)
            
            cargo = request.POST.get('cargo')
                
            intancePerfilColaborador(user_, cargo, 'Chamado por colaborador', 'analise', True)

            return redirect("home")
    else:
        form = PerfilColacoradorFormChamar()

    return render(request, 'add_gestores_buscar_user.html', {'perfil_colaborador': perfil_colaborador, 'user_': user_, 'dados_interacoes' : dados_interacoes,'dados_histrico' : dados_histrico, 'form': form})

def gestao_equipe_buscar(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
    else:
        return redirect("login")

    # Aqui vamos buscar os usuários reais
    users = User.objects.all()  # Supondo que todos os usuários devem ser listados
    perfis_colaboradores = getTodosPerfisColaborador()

    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        users = users.filter(
            username__icontains=search_query.lower()
        )

        user_list = [
            {'username': user.username, 'last_login': user.last_login, 'email': user.email} for user in users
        ]
        return JsonResponse({'users': user_list})

    return render(request, "gestao_equipe.html", {'perfil_colaborador': perfil_colaborador, 'perfis_colaboradores': perfis_colaboradores})

def gestao_equipe_buscar_user(request, user_id):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
        
    else:
        return redirect("login")
    # Obtém o objeto User com base no user_id
    user = get_object_or_404(User, pk=user_id)

    # Obtém o perfil do colaborador associado ao usuário
    perfil = get_object_or_404(PerfilColaborador, user=user)

    return render(request, 'gestao_equipe_buscar_user.html', {'perfil_colaborador': perfil_colaborador, 'perfil' : perfil})

def novos_membros_formulario_user(request, user_id):
    user_ = getUserById(user_id)

    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
        
    else:
        return redirect("login")

    # Obtém o perfil do colaborador associado ao usuário
    perfil = get_object_or_404(PerfilColaborador, user=user_)

    feedback_user = getFeedbacksUser(user_)
    reporte_user = getFormularioReporteUser(user_)
    suporte_user = getFormularioSuporteUser(user_)

    dados_interacoes = {
        'numero1' : int(feedback_user.count()),
        'numero2' : int (reporte_user.count() + suporte_user.count()),
    }
    
    historico_concluido = getHistoricoComcluido(user_)
    historico_incompleto = getHistoricoIncompletos(user_)

    dados_histrico = {
        'numero1' : int(historico_concluido.count()),
        'numero2' : int(historico_incompleto.count()),
    }

    if request.method == 'POST':
        submit_type = request.POST.get('submit_type')
        print("olhe" + submit_type)

        if submit_type == 'admitir':
            print(submit_type)
            setPerfilColaboradorAtividade(user_, True)
            return redirect("novos_membros_formulario")
        elif submit_type == 'negar':
            perfil.delete()
            return redirect("novos_membros_formulario")
        
    forms = FormularioVazio()

    return render(request, 'add_gestores_formulario_user.html', {'perfil_colaborador': perfil_colaborador, 'perfil' : perfil, 'dados_interacoes' : dados_interacoes,'dados_histrico' : dados_histrico, 'forms' : forms})

# def CriarFormularioMensagem(request):
    
#def remocao
def remocao(request, perfil_id):
    perfil = get_object_or_404(PerfilColaborador, id=perfil_id)

    if request.method == 'POST':
        motivo_remocao = request.POST.get('motivo_remocao')
        perfil.motivo_remocao = motivo_remocao
        perfil.save()

        perfil.delete()

        return redirect('gestao_equipe')

    return render(request, 'gestao_equipe_buscar_user.html', {'perfil': perfil})

def suporte_e_reporte(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return render(request, 'suporte_e_reporte.html')
    else:
        return redirect("login")
    
    # Recuperar todos os formulários de suporte e reporte criados
    formularios_suporte = FormularioSuporte.objects.filter(status=False)
    formularios_reporte = FormularioReporte.objects.filter(status=False)

    return render(request, 'suporte_e_reporte.html', {
        'perfil_colaborador': perfil_colaborador,
        'formularios_suporte': formularios_suporte,
        'formularios_reporte': formularios_reporte
    })

def configuracoes(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return render(request, 'configuracoes.html')
    else:
        return redirect("login")
    
    return render(request, 'configuracoes.html', {'perfil_colaborador': perfil_colaborador})

def gestao_titulos(request):
    if request.user.is_authenticated:
        try:
            perfil_colaborador = getPerfilColaborador(request)
        except PerfilColaborador.DoesNotExist:
            return redirect("home")
    else:
        return redirect("login")
    
    return render(request, 'gestao_titulos.html', {'perfil_colaborador': perfil_colaborador})

def alterar_cargo(request, perfil_id):
    perfil = get_object_or_404(PerfilColaborador, id=perfil_id)

    if request.method == 'POST':
        form = PerfilColacoradorForm(request.POST, instance=perfil)

        if form.is_valid():
            novo_cargo = form.cleaned_data['cargo']
            
            # Certifique-se de que o novo cargo é válido (você pode personalizar isso com base em seus valores permitidos)
            if novo_cargo in ['usuario_normal', 'outro_cargo1', 'outro_cargo2']:
                perfil.cargo = novo_cargo
                perfil.save()
                return redirect('gestao_equipe_buscar_user', user_id=perfil.user.id)
            else:
                form.add_error('cargo', 'Cargo inválido. Escolha uma opção válida.')

    else:
        form = PerfilColacoradorForm(instance=perfil)

    return render(request, 'gestao_equipe.html', {'form': form, 'perfil': perfil})




