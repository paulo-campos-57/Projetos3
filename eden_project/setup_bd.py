import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eden_project.settings')
django.setup()

from django.contrib.auth.models import User
from gestor.models import Midia

def criar_superuser(username_, email_, senha_):
    if not User.objects.filter(username = username_).exists():
        User.objects.create_superuser(username_, email_, senha_)

def criar_user(username_, email_, senha_):
    if not User.objects.filter(username = username_).exists():
        User.objects.create_user(username_, email_, senha_)

def configurar_bd():

    criar_superuser('admin', 'admin@example.com', '12345678')
    
    criar_user('usuario_teste', 'usuario_teste@example.com', 'senha_teste')

def main():
    print("Configurando o banco de dados de teste...")
    configurar_bd()
    print("Banco de dados de teste configurado com sucesso!")

if __name__ == "__main__":
    main()


"""
# setup_bd_teste.py

import argparse
from django.contrib.auth.models import User
from meuapp.models import SeuModelo

def configurar_bd_teste(usuario, email, senha):
    if not User.objects.filter(username=usuario).exists():
        User.objects.create_superuser(usuario, email, senha)

    SeuModelo.objects.create(campo1='valor1', campo2='valor2')

def configurar_apenas_modelo():
    SeuModelo.objects.create(campo1='valor1', campo2='valor2')

def outra_funcao(arg1, arg2):
    print(f"Executando outra função com argumentos: {arg1}, {arg2}")

def main():
    parser = argparse.ArgumentParser(description='Configurar banco de dados de teste')
    parser.add_argument('--modelo', action='store_true', help='Configurar apenas o modelo')
    parser.add_argument('--usuario', type=str, help='Nome de usuário para superusuário')
    parser.add_argument('--email', type=str, help='Endereço de e-mail para superusuário')
    parser.add_argument('--senha', type=str, help='Senha para superusuário')
    parser.add_argument('--outra', action='store_true', help='Executar outra função')
    parser.add_argument('--arg1', type=str, help='Argumento 1 para outra função')
    parser.add_argument('--arg2', type=int, help='Argumento 2 para outra função')
    args = parser.parse_args()

    if args.modelo:
        configurar_apenas_modelo()
    elif args.outra:
        if not all([args.arg1, args.arg2]):
            parser.error("Os argumentos --arg1 e --arg2 são necessários para a outra função.")
        outra_funcao(args.arg1, args.arg2)
    else:
        if not all([args.usuario, args.email, args.senha]):
            parser.error("Os argumentos --usuario, --email e --senha são necessários para configurar o superusuário.")
        configurar_bd_teste(args.usuario, args.email, args.senha)

    print("Banco de dados de teste configurado com sucesso!")

if __name__ == "__main__":
    main()


    


# Configurar apenas o modelo
python setup_bd_teste.py --modelo

# Configurar o superusuário
python setup_bd_teste.py --usuario admin --email admin@example.com --senha senha_admin

# Executar outra função
python setup_bd_teste.py --outra --arg1 valor1 --arg2 42

"""