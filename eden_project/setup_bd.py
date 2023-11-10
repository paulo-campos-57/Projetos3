import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eden_project.settings')
django.setup()

from django.contrib.auth.models import User
from gestor.models import Midia, PerfilColaborador

CARTAZ = "https://media.discordapp.net/attachments/1097961194427514930/1101128002768736286/not_found.png?ex=655f4a5d&is=654cd55d&hm=bdd0c3fec65aadbae16eacae003b2c35581650479b6ec5203f81ef5b01f867e8&=&width=1090&height=708"
MIDIA = "https://media.discordapp.net/attachments/1097961194427514930/1101128002768736286/not_found.png?ex=655f4a5d&is=654cd55d&hm=bdd0c3fec65aadbae16eacae003b2c35581650479b6ec5203f81ef5b01f867e8&=&width=1090&height=708"

def criar_superuser(username, email, senha):
    if not User.objects.filter(username = username).exists():
        User.objects.create_superuser(username, email, senha)
        return
    
    print(f"Usuário com username '{username}' já existe encontrado.")

def criar_user(username, email, senha):
    if not User.objects.filter(username = username).exists():
        User.objects.create_user(username, email, senha)
        return
    
    print(f"Usuário com username '{username}' já existe encontrado.")

def criar_midia(titulo, username, descricao, status, dataPostagem, arqMidiaPath, arqCartazPath):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Usuário com username '{username}' não encontrado.")
        return
    
    if Midia.objects.filter(titulo=titulo).exists():
        print(f"Uma instância da Midia com título '{titulo}' já existe. Não foi criada uma nova instância.")
        return

    midia = Midia(
        titulo=titulo,
        user=user,
        descricao=descricao,
        status=status,
        dataPostagem = dataPostagem,
        arqMidia=arqMidiaPath,
        arqCartaz=arqCartazPath
    )
    midia.save()

def criar_perfil_colaborador(username, cargo, status, atividade):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Usuário com username '{username}' não encontrado.")
        return
    
    if PerfilColaborador.objects.filter(user=user).exists():
        print(f"O usuário '{username}' já possui um perfil de colaborador. Não foi criada uma nova instância.")
        return
    
    perfil = PerfilColaborador(
        user=user,
        cargo=cargo,
        status=status,
        atividade=atividade
    )

    perfil.save()

def criar_bd_filmes():
    criar_user('Brian Knappenberger', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('We Are Legion', 'Brian Knappenberger', 'Este documentário nos leva para dentro do mundo do Anonymous, o grupo de hackers radicais que se tornou símbolo da desobediência civil na era digital.', 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Lívia Perez', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Quem Matou Eloá?', 'Lívia Perez', 'Em 2008, Lindemberg Alves de 22 anos invadiu o apartamento da ex-namorada Eloá Pimentel de 15 anos, armado, mantendo-a refém por cinco dias. O crime foi amplamente transmitido pelos canais de TV. “Quem matou Eloá?” traz uma análise crítica sobre a espetacularização da violência e a abordagem da mídia televisiva nos casos de violência contra a mulher, revelando um dos motivos pelo qual o Brasil é o quinto no ranking de países que mais matam mulheres.', 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Flávio Colombini', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('Lute Como uma Menina', 'Flávio Colombini', 'Este documentário conta a história das meninas que participaram do movimento secundarista que ocupou escolas e foi as ruas para lutar contra um projeto de reorganização escolar imposto pelo governador de São Paulo, que previa o fechamento de quase cem escolas.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Vi-Dan Tran', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2020, 1, 1, 12, 0, 0)
    criar_midia('Cyberpunk 2077: Phoenix Program', 'Vi-Dan Tran', 'Um fan filme de ação ambientado no universo de Cyberpunk 2077.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('William A. Wellman', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(1937, 1, 1, 12, 0, 0)
    criar_midia('A Star Is Born', 'William A. Wellman', 'A jovem Esther (Janet Gaynor) chega a Hollywood para tentar se tornar uma estrela do cinema. Quando conhece o astro Norman Maine (Fredric March), os dois logo se apaixonam e ele impulsiona a carreira da amada. No entanto, o relacionamento fica abalado quando o alcoolismo de Norman começa a interferir na carreira de Esther. Vencedor do Oscar de Melhor Roteiro Original.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Kellynson W. Mattos', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2021, 1, 1, 12, 0, 0)
    criar_midia('Catadores na Pandemia', 'Kellynson W. Mattos', 'O Documentário aborda a situação cotidiana de catadores de matérias recicláveis das cooperativas Cooper Glicério e Nova Glicério durante o período mais complicado da pandemia no Brasil e na cidade de São Paulo.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Victor Machado', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2019, 1, 1, 12, 0, 0)
    criar_midia('Lú', 'Victor Machado', 'Lú é uma jovem estudante de artes visuais que, após perder os pais, se vê na obrigação de cuidar do avô com depressão. Em meio a essa nova vida, repleta de novas responsabilidades, ela terá que aprender a lidar com seus próprios medos e encarar uma mudança expressiva em sua personalidade.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Paulo Munhoz', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2007, 1, 1, 12, 0, 0)
    criar_midia('Belowars', 'Paulo Munhoz', 'BELOWARS conta a história de BAITA, um garotinho de origem humilde que sonha em apreender a ARTE DA GUERRA. Sua aventura o leva a muitos lugares, ao encontro de muitas pessoas, ao enfrentamento da sua guerra interior.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime.datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('BRICHOS', 'Paulo Munhoz', 'Os BRICHOS - bichos brasileiros - precisam salvar a sua cidade - a Vila dos Brichos - de um ataque especulativo que quer transformar o seu sistema harmônico de tecnologia e natureza numa "moderna" Megalópole.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Ekatala Keller', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2020, 1, 1, 12, 0, 0)
    criar_midia('Casa 05: O Sol que nos habita', 'Ekatala Keller', 'Um documentário sobre arte, na voz de artistas consagrados que contam detalhes de suas histórias de vida e sobre ser artista, vivendo de arte no Brasil.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Alba Sotorra', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2018, 1, 1, 12, 0, 0)
    criar_midia('Comandante Arian', 'Alba Sotorra', 'Na linha de frente da guerra na Síria, uma comandante de 30 anos leva seu batalhão feminino a retomar uma cidade controlada pelo ISIS e emerge gravemente ferida, forçando-a a se redefinir nesse conto de libertação e liberdade.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Letícia Sabatella', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('Hotxuá', 'Letícia Sabatella', 'Um registro poético sobre a tribo indígena krahô, um povo sorridente que designa um sacerdote do riso, o hotxuá, para fortalecer e unir o grupo através da alegria, do abraço e da conversa' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Bruno Graziano', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('O Acre Existe', 'Bruno Graziano', 'Quatro paulistas partem para o Acre. O filme constrói, com encontros e vivências, um retrato contemporâneo do povo e da cultura acreana. Do road movie clássico, entra numa jornada onde se mistura aos ambientes e personagens. A partir dessas tensões, viaja da história do Estado ao Santo Daime; das tribos indígenas à herança de Chico Mendes; dos soldados da borracha ao Acre atual. O documentário expõe essa descoberta mútua entre os que chegam e os que lá estão.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Antonio Sagrado', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Quando Sinto Que Já Sei', 'Antonio Sagrado', 'O documentário “Quando sinto que já sei” registra práticas educacionais inovadoras que estão ocorrendo pelo Brasil. A obra reúne depoimentos de pais, alunos, educadores e profissionais de diversas áreas sobre a necessidade de mudanças no tradicional modelo de escola.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Allyson Alapont', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('O Que É Nosso', 'Allyson Alapont', 'Um documentário da cena única sobre as festas gratuitas e abertas de São Paulo, um movimento que mudou a cidade.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Daniela Fioravanti', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Amazônia, da impertinência à conciliação', 'Daniela Fioravanti', 'Conheça os territórios protegidos criados para preservar a floresta, as unidades de conservação: como funcionam, os benefícios que elas geram e as dificuldades para que cumpram a missão de manter a Amazônia em pé.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Kelly Nyks', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Disruption', 'Kelly Nyks', 'Quando se trata de mudanças climáticas, por que fazemos tão pouco quando sabemos tanto? Através de uma investigação incansável para encontrar a resposta, "A Ruptura" lança um olhar inflexível sobre as consequências devastadoras da nossa inação.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Pedro Serra', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Que Estranha Forma de Vida', 'Pedro Serra', 'Neste documentário serão abordadas formas de vida paralelas à sociedade tal como a conhecemos, que procuram viver em harmonia, com uma visão do futuro baseado na sustentabilidade e na cooperação entre o ser humano, animal e natureza.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Silvio Luiz Cordeiro', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Antiga Amazônia Presente', 'Silvio Luiz Cordeiro', 'Documentário e diário de bordo de uma expedição na Amazônia brasileira que procura entender sua realidade atual e passada a partir das vivências, caminhadas, conversas e sítios arqueológicos.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Charles Chaplin', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(1936, 1, 1, 12, 0, 0)
    criar_midia('Tempos Modernos', 'Charles Chaplin', 'Tempos Modernos é um filme de 1936 dos Estados Unidos do cineasta Charlie Chaplin em que o seu famoso personagem "O Vagabundo" tenta sobreviver em meio ao mundo moderno e industrializado.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Renato Tapajós', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(1980, 1, 1, 12, 0, 0)
    criar_midia('Linha de Montagem', 'Renato Tapajós', 'O filme registra as grandes greves dos metalúrgicos em 1978, 1979 e 1980, mostra os bastidores da luta sindical e acompanha de perto a ascensão de Lula como líder dos trabalhadores. Trata-se de um dos maiores registros da história do sindicalismo brasileiro e de como o ex-presidente Lula se tornou o líder de massas que é hoje.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Consuelo Lins', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2010, 1, 1, 12, 0, 0)
    criar_midia('Babás', 'Consuelo Lins', 'Fotografias, filmes de família, anúncios de jornais do século XX constroem uma narrativa pessoal sobre a presença das babás no cotidiano de inúmeras famílias brasileiras, mostrando uma situação em que o afeto é genuíno, mas não dissolve a violência.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Daniela Muzi', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2017, 1, 1, 12, 0, 0)
    criar_midia('O Que Nos Move', 'Daniela Muzi', 'A cada quatro anos brasileiros e brasileiras de todo o país se reúnem para defender o direito à saúde, mas em 2015 a Conferência Nacional de Saúde não tratou apenou da saúde da população, tratou também da saúde da democracia.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Fritz Lang', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(1927, 1, 1, 12, 0, 0)
    criar_midia('Metrópolis', 'Fritz Lang', 'Uma cidade futurista chamada Metropolis dividida entre a classe trabalhadora e os planejadores da cidade, o filho do mestre da cidade se apaixona por uma profeta da classe trabalhadora, que prevê a vinda de um salvador para mediar a diferença entre as classes.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Hannu Puttonen', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2001, 1, 1, 12, 0, 0)
    criar_midia('The Code', 'Hannu Puttonen', 'The Code é um documentário finlandês sobre GNU/Linux a partir de 2001, com algumas das pessoas mais influentes do movimento software livre.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Fernando Grostein Andrade', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2011, 1, 1, 12, 0, 0)
    criar_midia('Quebrando o Tabu', 'Fernando Grostein Andrade', 'O filme propõe um debate sério e bem informado sobre o complexo problema das drogas no Brasil e no mundo. Participações de Fernando Henrique Cardoso, Bill Clinton, Jimmy Carter, Drauzio Varella e Paulo Coelho.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Kevin Macdonald', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('Life in a Day', 'Kevin Macdonald', 'O filme é formado por vídeos de homens e mulheres ao redor do mundo que filmaram um dia de suas vidas. Um documentário diferente, que reflete as belezas da vida.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('German Doin', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('A Educação Proibida', 'German Doin', 'Documentário que se propõe a questionar as lógicas da escolarização moderna e a forma de entender a educação, mostrando diferentes experiências educativas, não convencionais, que propõem a necessidade de um novo modelo educativo.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Simon Klose', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2013, 1, 1, 12, 0, 0)
    criar_midia('The Pirate Bay AFK', 'Simon Klose', 'Documentário sobre a vida dos três fundadores do site de compartilhamento de arquivos The Pirate Bay, dirigido por Simon Klose.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Sini Anderson', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2013, 1, 1, 12, 0, 0)
    criar_midia('The Punk Singer', 'Sini Anderson', 'Documentário sobre a ativista e ícone cultural Kathleen Hanna, que formou a banda punk Bikini Kill e foi pioneira do movimento "Riot Grrrl" durante a década de 1990.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime.datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('O Menino da Internet', 'Brian Knappenberger', 'A história do ativista de internet e pioneiro de programação Aaron Swartz a partir de sua adolescencia, seu envolvimento com o RSS, a fundação do Reddit, e seu crescente interesse na defesa política relacionada a Cultura Livre. O filme ainda explora sua prisão, as táticas da acusação a fundamentar seus supostos crimes.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Jason Bertrand ', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Grounded', 'Jason Bertrand ', 'Neste documentário você vai ver algumas da técnicas usadas no desenvolvimento e criação do jogo que foi um dos mais aclamados pela crítica em 2013 . The Last of Us é o jogo mais premiado da história dos jogos com mais de 231 prêmios' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Pedro Fávero', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('O Rap Pelo Rap', 'Pedro Fávero', 'Para fazer este documentário, o diretor contou com 42 personagens - entre MCs, DJs e produtores - para traçar um panorama do gênero no país. Eles falam aqui abertamente sobre os 8 temas propostos pelo filme e procuram entender o Rap. Rap bom é rap antigo? Rap e mídia combinam? Qual o futuro do Rap nacional? Ninguém melhor para debater essas perguntas que o próprio Rap. Desde os primeiros a se arriscar no estilo, até os mais recentes astros do underground. Um filme para os aspirantes à MC/DJ/produtor, fãs do gênero e interessados na cultura.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('José Marques de Carvalho Jr', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('Observar e Absorver', 'José Marques de Carvalho Jr', '"Eu sou extremamente ambicioso. Eu sou ambicioso de uma forma que ninguém pode conceber. Porque dinheiro, conforto, estabilidade, luxo, pra mim é pouco, eu quero mais. Eu quero tudo que eu puder levar dessa vida" por Eduardo Marinho' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Jonathan Schiefer', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Algorithm', 'Jonathan Schiefer', 'Depois de descobrir um grande projeto secreto da NSA, um hacker freelancer precisa escolher entre sua curiosidade ou a segurança de seus amigos.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('Pedro Ekman', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('Freenet', 'Pedro Ekman', 'O quanto somos realmente livres na internet para acessar conteúdos, e nos expressarmos? Quem governa a rede? Com quais interesses? Temos privacidade? Quem garante o direito de todos os cidadãos a uma conexão rápida e de baixo custo?' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime.datetime(2017, 1, 1, 12, 0, 0)
    criar_midia('Desperdício Desperdiçado', 'Pedro Serra', 'Documentário sobre estilos de vida Freegan, baseados no boicote ao capitalismo, rejeitando qualquer forma de exploração animal ou humana, através do consumo limitado e consciente de recursos, bem como o resgate de desperdício, procurando soluções sustentáveis, numa sociedade que produz acima das suas necessidades.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    criar_user('aa', 'filmes@exemple.com', 'senha_filmes')
    dataFilme = datetime.datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('bb', 'aa', '#' , 'aprovado', dataFilme, CARTAZ, MIDIA)


def configurar_bd():

    criar_superuser('Gilmor', 'admin@example.com', '12345678')
    
    criar_user('MarcosSerra', 'marquinhosserragens@gmail.com', 'senha_teste')

    criar_bd_filmes()

    criar_perfil_colaborador('MarcosSerra', 'reportuser', 'analise', 'False')

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