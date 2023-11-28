import os
import django
from datetime import datetime, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eden_project.settings')
django.setup()

from django.contrib.auth.models import User
from gestor.models import  Midia, PerfilColaborador, UserHistorico, FormularioSuporte, FormularioReporte, UserFeedback, Mensagens
from django.utils import timezone

CARTAZ = "https://media.discordapp.net/attachments/1097961194427514930/1101128002768736286/not_found.png?ex=655f4a5d&is=654cd55d&hm=bdd0c3fec65aadbae16eacae003b2c35581650479b6ec5203f81ef5b01f867e8&=&width=1090&height=708"
MIDIA = "https://media.discordapp.net/attachments/1097961194427514930/1101128002768736286/not_found.png?ex=655f4a5d&is=654cd55d&hm=bdd0c3fec65aadbae16eacae003b2c35581650479b6ec5203f81ef5b01f867e8&=&width=1090&height=708"

def criar_superuser(username, email, senha, first_name, last_name):
    if not User.objects.filter(username = username).exists():
        user = User.objects.create_superuser(username, email, senha)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return
    
    print(f"Usuário com username '{username}' já existe encontrado.")

def criar_user(username, email, senha, first_name, last_name):
    if not User.objects.filter(username = username).exists():
        user = User.objects.create_user(username, email, senha)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return
    
    print(f"Usuário com username '{username}' já existe encontrado.")

def criar_midia(titulo, username, autor, descricao, status, dataPostagem, arqMidiaPath, arqCartazPath):
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
        autor = autor,
        descricao=descricao,
        status=status,
        dataPostagem = dataPostagem,
        arqMidia=arqMidiaPath,
        arqCartaz=arqCartazPath
    )
    midia.save()

def criar_historico(username, titulo, dataHistorico, concluido):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Usuário com username '{username}' não encontrado.")
        return

    try:
        midia = Midia.objects.get(titulo=titulo)
    except Midia.DoesNotExist:
        print(f"Mídia de título '{titulo}' não encontrada.")
        return
    
    if UserHistorico.objects.filter(user=user).filter(midia=midia).exists():
        print(f"O histórico de '{titulo}' para o user '{username}' já existe")
        return
    
    historico = UserHistorico(
        user=user,
        midia=midia,
        concluido=concluido,
        dataHistorico=dataHistorico
    )
    
    historico.save()

def formulario_suporte(username,texto,status):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Usuário com username '{username}' não encontrado.")
        return
    
    if FormularioSuporte.objects.filter(user=user).filter(status=True).exists():
        print(f"O usuario '{username}' já abriu suporte")
        return

    formulario = FormularioSuporte(
        user=user,
        texto=texto,
        status=status
    )
    
    formulario.save()

def formulario_reporte(username, categoriaReporte, midia, texto, status):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Usuário com username '{username}' não encontrado.")
        return
    
    if FormularioReporte.objects.filter(username=username).exists():
        print(f"Uma instância de formulário reporte do usuário '{username}' já existe. Não foi criada uma nova instância.")
        return

    formulario = FormularioReporte(
        user = user,
        categoriaReporte = categoriaReporte,
        midia = midia,
        texto = texto,
        status = status
    )
    formulario.save()

def user_feedback(username,titulo,reacao,comentario):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Usuário com username '{username}' não encontrado.")
        return
    
    try:
        midia = Midia.objects.get(titulo=titulo)
    except Midia.DoesNotExist:
        print(f"Mídia de título '{titulo}' não encontrada.")
        return
    
    if UserFeedback.objects.filter(user=user).filter(midia=midia).exists():
        print(f"O feedback de '{titulo}' pelo user '{username}' já existe")
        return
    
    feedback=UserFeedback(
        reacao=reacao,
        user=user,
        comentario=comentario,
        midia=midia 
        )
    
    feedback.save()

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

def criar_mensagem(username, user_destino_username, mensagem, contexto, dataMensagem):
    try:
        user = User.objects.get(username=username)
        
    except User.DoesNotExist:
        print(f"Usuário com username '{username}' não encontrado.")
        return
    
    try:
        user_destino = User.objects.get(username=user_destino_username)
        
    except User.DoesNotExist:
        print(f"Usuário com username '{user_destino_username}' não encontrado.")
        return

    mensagem = Mensagens(
        user=user,
        user_destino= user_destino,
        mensagem=mensagem,
        contexto=contexto,
        dataMensagem = dataMensagem
    )
    mensagem.save()

def criar_bd_mensagens():
    dataMensagem = datetime(2014, 1, 1, 12, 30, 20)
    criar_mensagem('MarcosSerra', 'Gilmor', 'Olá desejo um cargo de adiministrador de Suporte e Reporte', 'Pedido_de_cargo', dataMensagem)

def criar_bd_formulario_reporte():
    formulario_reporte('MarcosSerra', 'Problema_de_Legenda', 'We Are Legion', 'Este título não está com a legenda sincronizada, além da tradução estar errada.', 'False')

def criar_bd_filmes():
    dataFilme = datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('We Are Legion', 'Gilmor', 'Brian Knappenberger', 'Este documentário nos leva para dentro do mundo do Anonymous, o grupo de hackers radicais que se tornou símbolo da desobediência civil na era digital.', 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Quem Matou Eloá?', 'Gilmor', 'Lívia Perez', 'Em 2008, Lindemberg Alves de 22 anos invadiu o apartamento da ex-namorada Eloá Pimentel de 15 anos, armado, mantendo-a refém por cinco dias. O crime foi amplamente transmitido pelos canais de TV. “Quem matou Eloá?” traz uma análise crítica sobre a espetacularização da violência e a abordagem da mídia televisiva nos casos de violência contra a mulher, revelando um dos motivos pelo qual o Brasil é o quinto no ranking de países que mais matam mulheres.', 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('Lute Como uma Menina', 'Gilmor', 'Flávio Colombini', 'Este documentário conta a história das meninas que participaram do movimento secundarista que ocupou escolas e foi as ruas para lutar contra um projeto de reorganização escolar imposto pelo governador de São Paulo, que previa o fechamento de quase cem escolas.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2020, 1, 1, 12, 0, 0)
    criar_midia('Cyberpunk 2077: Phoenix Program', 'Gilmor', 'Vi-Dan Tran', 'Um fan filme de ação ambientado no universo de Cyberpunk 2077.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(1937, 1, 1, 12, 0, 0)
    criar_midia('A Star Is Born', 'Gilmor', 'William A. Wellman', 'A jovem Esther (Janet Gaynor) chega a Hollywood para tentar se tornar uma estrela do cinema. Quando conhece o astro Norman Maine (Fredric March), os dois logo se apaixonam e ele impulsiona a carreira da amada. No entanto, o relacionamento fica abalado quando o alcoolismo de Norman começa a interferir na carreira de Esther. Vencedor do Oscar de Melhor Roteiro Original.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2021, 1, 1, 12, 0, 0)
    criar_midia('Catadores na Pandemia', 'Gilmor', 'Kellynson W. Mattos', 'O Documentário aborda a situação cotidiana de catadores de matérias recicláveis das cooperativas Cooper Glicério e Nova Glicério durante o período mais complicado da pandemia no Brasil e na cidade de São Paulo.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2019, 1, 1, 12, 0, 0)
    criar_midia('Lú', 'Gilmor', 'Victor Machado', 'Lú é uma jovem estudante de artes visuais que, após perder os pais, se vê na obrigação de cuidar do avô com depressão. Em meio a essa nova vida, repleta de novas responsabilidades, ela terá que aprender a lidar com seus próprios medos e encarar uma mudança expressiva em sua personalidade.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2007, 1, 1, 12, 0, 0)
    criar_midia('Belowars', 'Gilmor', 'Paulo Munhoz', 'BELOWARS conta a história de BAITA, um garotinho de origem humilde que sonha em apreender a ARTE DA GUERRA. Sua aventura o leva a muitos lugares, ao encontro de muitas pessoas, ao enfrentamento da sua guerra interior.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('BRICHOS', 'Gilmor', 'Paulo Munhoz', 'Os BRICHOS - bichos brasileiros - precisam salvar a sua cidade - a Vila dos Brichos - de um ataque especulativo que quer transformar o seu sistema harmônico de tecnologia e natureza numa "moderna" Megalópole.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2020, 1, 1, 12, 0, 0)
    criar_midia('Casa 05: O Sol que nos habita', 'Gilmor', 'Ekatala Keller', 'Um documentário sobre arte, na voz de artistas consagrados que contam detalhes de suas histórias de vida e sobre ser artista, vivendo de arte no Brasil.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2018, 1, 1, 12, 0, 0)
    criar_midia('Comandante Arian', 'Gilmor', 'Alba Sotorra', 'Na linha de frente da guerra na Síria, uma comandante de 30 anos leva seu batalhão feminino a retomar uma cidade controlada pelo ISIS e emerge gravemente ferida, forçando-a a se redefinir nesse conto de libertação e liberdade.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('Hotxuá', 'Gilmor', 'Letícia Sabatella', 'Um registro poético sobre a tribo indígena krahô, um povo sorridente que designa um sacerdote do riso, o hotxuá, para fortalecer e unir o grupo através da alegria, do abraço e da conversa' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('O Acre Existe', 'Gilmor', 'Bruno Graziano', 'Quatro paulistas partem para o Acre. O filme constrói, com encontros e vivências, um retrato contemporâneo do povo e da cultura acreana. Do road movie clássico, entra numa jornada onde se mistura aos ambientes e personagens. A partir dessas tensões, viaja da história do Estado ao Santo Daime; das tribos indígenas à herança de Chico Mendes; dos soldados da borracha ao Acre atual. O documentário expõe essa descoberta mútua entre os que chegam e os que lá estão.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Quando Sinto Que Já Sei', 'Gilmor', 'Antonio Sagrado', 'O documentário “Quando sinto que já sei” registra práticas educacionais inovadoras que estão ocorrendo pelo Brasil. A obra reúne depoimentos de pais, alunos, educadores e profissionais de diversas áreas sobre a necessidade de mudanças no tradicional modelo de escola.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('O Que É Nosso', 'Gilmor', 'Allyson Alapont', 'Um documentário da cena única sobre as festas gratuitas e abertas de São Paulo, um movimento que mudou a cidade.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Amazônia, da impertinência à conciliação', 'Gilmor', 'Daniela Fioravanti', 'Conheça os territórios protegidos criados para preservar a floresta, as unidades de conservação: como funcionam, os benefícios que elas geram e as dificuldades para que cumpram a missão de manter a Amazônia em pé.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Disruption', 'Gilmor', 'Kelly Nyks', 'Quando se trata de mudanças climáticas, por que fazemos tão pouco quando sabemos tanto? Através de uma investigação incansável para encontrar a resposta, "A Ruptura" lança um olhar inflexível sobre as consequências devastadoras da nossa inação.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Que Estranha Forma de Vida', 'Gilmor', 'Pedro Serra', 'Neste documentário serão abordadas formas de vida paralelas à sociedade tal como a conhecemos, que procuram viver em harmonia, com uma visão do futuro baseado na sustentabilidade e na cooperação entre o ser humano, animal e natureza.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Antiga Amazônia Presente', 'Gilmor', 'Silvio Luiz Cordeiro', 'Documentário e diário de bordo de uma expedição na Amazônia brasileira que procura entender sua realidade atual e passada a partir das vivências, caminhadas, conversas e sítios arqueológicos.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(1936, 1, 1, 12, 0, 0)
    criar_midia('Tempos Modernos', 'Gilmor', 'Charles Chaplin', 'Tempos Modernos é um filme de 1936 dos Estados Unidos do cineasta Charlie Chaplin em que o seu famoso personagem "O Vagabundo" tenta sobreviver em meio ao mundo moderno e industrializado.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(1980, 1, 1, 12, 0, 0)
    criar_midia('Linha de Montagem', 'Gilmor','Renato Tapajós', 'O filme registra as grandes greves dos metalúrgicos em 1978, 1979 e 1980, mostra os bastidores da luta sindical e acompanha de perto a ascensão de Lula como líder dos trabalhadores. Trata-se de um dos maiores registros da história do sindicalismo brasileiro e de como o ex-presidente Lula se tornou o líder de massas que é hoje.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2010, 1, 1, 12, 0, 0)
    criar_midia('Babás', 'Gilmor', 'Consuelo Lins', 'Fotografias, filmes de família, anúncios de jornais do século XX constroem uma narrativa pessoal sobre a presença das babás no cotidiano de inúmeras famílias brasileiras, mostrando uma situação em que o afeto é genuíno, mas não dissolve a violência.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2017, 1, 1, 12, 0, 0)
    criar_midia('O Que Nos Move', 'Gilmor', 'Daniela Muzi', 'A cada quatro anos brasileiros e brasileiras de todo o país se reúnem para defender o direito à saúde, mas em 2015 a Conferência Nacional de Saúde não tratou apenou da saúde da população, tratou também da saúde da democracia.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(1927, 1, 1, 12, 0, 0)
    criar_midia('Metrópolis', 'Gilmor', 'Fritz Lang', 'Uma cidade futurista chamada Metropolis dividida entre a classe trabalhadora e os planejadores da cidade, o filho do mestre da cidade se apaixona por uma profeta da classe trabalhadora, que prevê a vinda de um salvador para mediar a diferença entre as classes.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2001, 1, 1, 12, 0, 0)
    criar_midia('The Code', 'Gilmor', 'Hannu Puttonen', 'The Code é um documentário finlandês sobre GNU/Linux a partir de 2001, com algumas das pessoas mais influentes do movimento software livre.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2011, 1, 1, 12, 0, 0)
    criar_midia('Quebrando o Tabu', 'Gilmor', 'Fernando Grostein Andrade', 'O filme propõe um debate sério e bem informado sobre o complexo problema das drogas no Brasil e no mundo. Participações de Fernando Henrique Cardoso, Bill Clinton, Jimmy Carter, Drauzio Varella e Paulo Coelho.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('Life in a Day', 'Gilmor', 'Kevin Macdonald', 'O filme é formado por vídeos de homens e mulheres ao redor do mundo que filmaram um dia de suas vidas. Um documentário diferente, que reflete as belezas da vida.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('A Educação Proibida', 'Gilmor', 'German Doin', 'Documentário que se propõe a questionar as lógicas da escolarização moderna e a forma de entender a educação, mostrando diferentes experiências educativas, não convencionais, que propõem a necessidade de um novo modelo educativo.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2013, 1, 1, 12, 0, 0)
    criar_midia('The Pirate Bay AFK', 'Gilmor', 'Simon Klose', 'Documentário sobre a vida dos três fundadores do site de compartilhamento de arquivos The Pirate Bay, dirigido por Simon Klose.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2013, 1, 1, 12, 0, 0)
    criar_midia('The Punk Singer', 'Gilmor', 'Sini Anderson', 'Documentário sobre a ativista e ícone cultural Kathleen Hanna, que formou a banda punk Bikini Kill e foi pioneira do movimento "Riot Grrrl" durante a década de 1990.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('O Menino da Internet', 'Gilmor', 'Brian Knappenberger', 'A história do ativista de internet e pioneiro de programação Aaron Swartz a partir de sua adolescencia, seu envolvimento com o RSS, a fundação do Reddit, e seu crescente interesse na defesa política relacionada a Cultura Livre. O filme ainda explora sua prisão, as táticas da acusação a fundamentar seus supostos crimes.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Grounded', 'Gilmor', 'Jason Bertrand ', 'Neste documentário você vai ver algumas da técnicas usadas no desenvolvimento e criação do jogo que foi um dos mais aclamados pela crítica em 2013 . The Last of Us é o jogo mais premiado da história dos jogos com mais de 231 prêmios' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('O Rap Pelo Rap', 'Gilmor', 'Pedro Fávero', 'Para fazer este documentário, o diretor contou com 42 personagens - entre MCs, DJs e produtores - para traçar um panorama do gênero no país. Eles falam aqui abertamente sobre os 8 temas propostos pelo filme e procuram entender o Rap. Rap bom é rap antigo? Rap e mídia combinam? Qual o futuro do Rap nacional? Ninguém melhor para debater essas perguntas que o próprio Rap. Desde os primeiros a se arriscar no estilo, até os mais recentes astros do underground. Um filme para os aspirantes à MC/DJ/produtor, fãs do gênero e interessados na cultura.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('Observar e Absorver', 'Gilmor', 'José Marques de Carvalho Jr', '"Eu sou extremamente ambicioso. Eu sou ambicioso de uma forma que ninguém pode conceber. Porque dinheiro, conforto, estabilidade, luxo, pra mim é pouco, eu quero mais. Eu quero tudo que eu puder levar dessa vida" por Eduardo Marinho' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Algorithm', 'Gilmor', 'Jonathan Schiefer', 'Depois de descobrir um grande projeto secreto da NSA, um hacker freelancer precisa escolher entre sua curiosidade ou a segurança de seus amigos.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('Freenet', 'Gilmor', 'Pedro Ekman', 'O quanto somos realmente livres na internet para acessar conteúdos, e nos expressarmos? Quem governa a rede? Com quais interesses? Temos privacidade? Quem garante o direito de todos os cidadãos a uma conexão rápida e de baixo custo?' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2017, 1, 1, 12, 0, 0)
    criar_midia('Desperdício Desperdiçado', 'Gilmor', 'Pedro Serra', 'Documentário sobre estilos de vida Freegan, baseados no boicote ao capitalismo, rejeitando qualquer forma de exploração animal ou humana, através do consumo limitado e consciente de recursos, bem como o resgate de desperdício, procurando soluções sustentáveis, numa sociedade que produz acima das suas necessidades.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2010, 1, 1, 12, 0, 0)
    criar_midia('Eu Não Quero Voltar Sozinho', 'Gilmor', 'Daniel Ribeiro', 'A vida de Leonardo, um adolescente deficiente visual, muda com a chegada de Gabriel, um novo aluno em sua escola. O jovem vive a inocência da descoberta do amor e da homossexualidade, ao mesmo tempo em que lida com o ciúme da amiga Giovana.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('O Fim do Recreio', 'Gilmor', 'Vinicius Mazzon', 'No Congresso Nacional, um projeto de lei pretende acabar com o recreio escolar. Ao mesmo tempo, em uma escola municipal de Curitiba, um grupo de crianças pode mudar toda essa história. Recheado de vibrantes brincadeiras infantis, O Fim do Recreio é um curta-metragem para todos os públicos, que bota a boca no trombone e avisa: cobra parada não engole sapo!' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2013, 1, 1, 12, 0, 0)
    criar_midia('Tem Gringo no Morro', 'Gilmor', 'Bruno Graziano', 'Um retrato do turismo estrangeiro na Rocinha, considerada a maior favela da América Latina e que recebe mais de 3000 gringos todos os meses. Eles vem interessados pelos mais diversos aspectos; da pobreza à violência, da geografia à arquitetura, da paisagem ao calor humano, da curiosidade ao assistencialismo.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('O Nostalgista', 'Gilmor', 'Giacomo Cimini', 'Em uma cidade do futuro, um pai precisa pegar estrada em busca de uma reposição para seu dispositivo de realidade virtual.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Quando Parei de Me Preocupar com Canalhas', 'Gilmor', 'Tiago Vieira', 'João Carlos se acha politizado, mas começa se dar conta de que vem se tornando tão chato quanto os taxistas da cidade. Enquanto esse fantasma o persegue e uma crise de relacionamento o leva ao fundo do poço, um surto de lucidez faz com que tome a decisão mais importante de sua vida.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('NoisDaRua', 'Gilmor', 'Fabiano Keller', '10 anos após os primeiros ataques a moradores de rua na Praça da Sé, em São Paulo, este documentário ouve as vozes das pessoas em situação de rua e seus sentimentos.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Crack, repensar', 'Gilmor', 'Felipe Crepker Vieira', 'Em uma sociedade de dependentes, questões como a redução de danos, internação compulsória e regulação das drogas precisam ser repensadas. Essa é a proposta do documentário Crack, repensar, que reúne depoimentos de usuários, ex-usuários, especialistas em saúde pública, acadêmicos, gestores e profissionais que atuam na promoção da justiça em um polêmico debate sobre como conviver com as drogas uma sociedade dependente.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2017, 1, 1, 12, 0, 0)
    criar_midia('Hotel Laide', 'Gilmor', 'Debora Diniz', 'Hotel Laide foi um dos mais importantes hotéis sociais da política de redução de danos para os usuários de crack da maior Cracolândia da América Latina. Um incêndio o destruiu, como em um anúncio da destruição que assombraria São Paulo com a política de prisão e internação para os usuários de crack.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(1984, 1, 1, 12, 0, 0)
    criar_midia('JANGO', 'Gilmor', 'Silvio Tendler', 'O filme refaz a trajetória política de João Goulart, o 24° presidente brasileiro, que foi deposto por um golpe militar nas primeiras horas de 1º de abril de 1964. Goulart era popularmente chamado de "Jango", daí o título do filme, lançado exatos vinte anos após o golpe.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2001, 1, 1, 12, 0, 0)
    criar_midia('Marighella', 'Gilmor', 'Silvio Tendler', 'Deputado constituinte de 46 e um dos principais dirigentes do Partido Comunista - cassado quando o partido foi posto na ilegalidade, Carlos Marighella foi um dos líderes da luta armada contra a ditadura militar no Brasil. Ainda no PC, em 66, propôs o caminho da guerrilha e por isso foi expulso. Fundou a Ação Libertadora Nacional, primeiro movimento armado pós-64 do país. O filme sobre a vida desta figura polêmica da recente História do Brasil contará a trajetória do professor Marighella. Mas, acima de tudo, contará a história do homem Marighella.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2013, 1, 1, 12, 0, 0)
    criar_midia('Verdade 12.528', 'Gilmor', 'Paula Sacchetta', 'O documentário "Verdade 12.528" trata da importância da Comissão Nacional da Verdade, através de depoimentos de vítimas da repressão, ex-presos políticos e outras pessoas afetadas direta ou indiretamente pela ditadura civil e militar entre 1964 e 1985.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Os Advogados contra a Ditadura', 'Gilmor', 'Silvio Tendler', 'Com a instauração da ditadura civil militar através de um golpe das Forças Armadas do Brasil, no período entre 1964 e 1985, o papel dos advogados na defesa dos direitos e garantias dos cidadãos foi fundamental no confronto com a repressão, ameaças e todo tipo de restrições.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('Em Busca da Verdade', 'Gilmor', 'Deraldo Goulart', 'Documentário apresenta as principais investigações da Comissão Nacional e das Comissões Estaduais da Verdade sobre as graves violações de direitos humanos ocorridas na ditadura de 1964.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('Filhos da Ditadura', 'Gilmor', 'Emanuelle Menezes', 'Filhos da Ditadura resgata a história dos brasileiros que desde muito cedo vivenciaram os prejuízos e os traumas de se viver em um ambiente antidemocrático. São vozes de um país que precisa, mais do que nunca, conhecer seu passado para entender seu presente e não repetir o mesmo erro no futuro.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2017, 1, 1, 12, 0, 0)
    criar_midia('Cúmplices?', 'Gilmor', 'Thomas Aders', 'Documentário da TV pública alemã que faz um levantamento histórico das atividades da VW do Brasil e suas relações com a ditadura militar brasileira.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2018, 1, 1, 12, 0, 0)
    criar_midia('Conservadorismo em Foco', 'Gilmor', 'Arthur Moura', 'Um filme sobre a ideologia burguesa e suas formas de dominação. O filme expõe o processo histórico de formação do conservadorismo na Europa e nos EUA a partir da década de 30 e acompanha seus desdobramentos até os dias atuais no Brasil.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2017, 1, 1, 12, 0, 0)
    criar_midia('XPLOIT', 'Gilmor', 'Fabrício Lima', 'A série introduz o espectador nas disputas políticas e econômicas que trazemconsequências diretas em nossos direitos essenciais dentro e fora do mundo digital.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2016, 1, 1, 12, 0, 0)
    criar_midia('Rarefeito', 'Gilmor', 'Marçal do Carmo', 'Cristian abandonou a família para escalar o Monte Everest e agora retorna para casa com câncer terminal. O retorno de Cristian traz à tona sua conturbada relação familiar e toda a situação socialmente instalada no Brasil: ele é o décimo quarto brasileiro a ter escalado o monte Everest. Mas o primeiro negro dentre eles.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2019, 1, 1, 12, 0, 0)
    criar_midia('Sob Evidências', 'Gilmor', 'Ronildo Garcia', 'Na pacata cidade de Ancila, a detetive Laura Lopes tenta conviver com o desaparecimento da filha Maria, adaptar-se com seu novo parceiro temperamental e desvendar os casos de um assassino em série.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2006, 1, 1, 12, 0, 0)
    criar_midia('Roube Este Filme', 'Gilmor', 'Jamie King', 'Roube Este Filme é um clássico documentário feito inicialmente para ser compartilhado e copiado pela rede torrent. O filme traz questões como propriedade intelectual, downloads e tecnologia.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2007, 1, 1, 12, 0, 0)
    criar_midia('Roube Este Filme 2', 'Gilmor', 'Jamie King', 'Continuação do documentário sobre o compartilhamento de arquivos, "pirataria" e cultura digital.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2009, 1, 1, 12, 0, 0)
    criar_midia('O Mínimo Existencial', 'Gilmor', 'José Marques de Carvalho Jr', 'O Mínimo Existencial é um documentário experimental dirigido e produzido por José Marques de Carvalho Jr. Filmado em 2009, o filme apresenta retalhos de entrevistas, e do cotidiano de moradores de um Rio de Janeiro em preto e branco.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2010, 1, 1, 12, 0, 0)
    criar_midia('Xetá', 'Gilmor', 'Fernando Severo', 'Durante o desordenado processo de colonização do noroeste do Paraná, nos anos 40 e 50, foi avistada uma população indígena que até então havia tido pouquíssimo contato com o homem branco. Logo o povo Xetá foi expulso de suas terras, vitimado por ações de extermínio e, os poucos sobreviventes, dispersos para outros locais. A quase extinção dos Xetá acabou contribuindo para provocar um desastre ecológico irreversível na região.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2011, 1, 1, 12, 0, 0)
    criar_midia('Remixofagia', 'Gilmor', 'Rodrigo Savazoni', 'Remixofagia é um documentário experimental sobre as lutas e ideias de uma nova cultura digital que emergia no Brasil na primeira década do século XXI.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2012, 1, 1, 12, 0, 0)
    criar_midia('Olhar Contestado', 'Gilmor', 'Fabianne Balvedi', 'Com proporções e significado semelhantes, a Guerra do Contestado conflagrou-se numa região do sul do Brasil cuja posse era disputada pelos estados do Paraná e Santa Catarina.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2013, 1, 1, 12, 0, 0)
    criar_midia('Nuvens de Veneno', 'Gilmor', 'Beto Novaes', 'A nuvem se espraia pelas plantações. Em vez de molhar, seca. Ela não traz a chuva, traz o veneno. O Brasil é um dos maiores produtores mundiais de soja, algodão, milho e também um dos maiores consumidores de fertilizantes químicos e agrotóxicos. Nuvens de veneno expõe as preocupações com as consequências do uso desses agroquímicos no ambiente, especialmente, na saúde do trabalhador. Um documentário revelador que faz refletir sobre a forma que crescemos e sobre o tipo de desenvolvimento que queremos.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Por Um Sonho Urbano', 'Gilmor', 'Edye Wilson', 'Por um sonho urbano conta a história das mais de vinte famílias que moram na Ocupação Saraí, um prédio abandonado no Centro de Porto Alegre, entre as ruas Caldas Júnior e Mauá. O documentário também retrata o dia a dia dos moradores, as suas atividades de rotina, o funcionamento do coletivo e as ações de luta pelo direito de morar à luz do movimento nacional de luta pela moradia.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('A Manada', 'Gilmor', 'Melanie Light', 'Este curta de horror vegano-feminista conta a história de mulheres presas em um lugar imundo para fornecerem seu leite materno.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2014, 1, 1, 12, 0, 0)
    criar_midia('Palhaços Anônimos', 'Gilmor', 'Gabriel do Valle', 'Respeitável público, apresentamos o drama dos palhaços que perceberam que a lágrima nunca é vazia, mas o riso pode ser. Quando cada riso da platéia parecer um riso a menos em seu coração, é hora de visitar a sala de terapia dos Palhaços Anônimos.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

    dataFilme = datetime(2015, 1, 1, 12, 0, 0)
    criar_midia('A Bicicleta de Kant', 'Gilmor', 'L. H. Girarde', 'LA Bicicleta de Kant é a representação imagética do pressuposto de que a vida é a projeção dos eventos que vivenciamos. Natureza, luz, céu, humanidade, guerra, destruição, vida e morte, tudo é projetado para descobrir o que há além do campo dos fenômenos, ou pelo menos, nos deixar com essa pergunta na mente.' , 'aprovado', dataFilme, CARTAZ, MIDIA)

def criar_atividade_user(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Usuário com username '{username}' não encontrado.")
        return
    
    numFilmes = random.randint(41, 57)
    numFilmesMes = random.randint(3, 5)

    midias = Midia.objects.order_by('?').all()

    count = 0

    for midia in midias:
        if (count < numFilmes):
            dataAtual = timezone.now()
            dataHistorico = dataAtual - timedelta(days=random.randint(30, 365))

            concluido = bool(random.randint(0, 1))

            criar_historico(username, midia.titulo, dataHistorico, concluido)

            count += 1
        elif (count < numFilmes + numFilmesMes):
            dataAtual = timezone.now()
            dataHistorico = dataAtual - timedelta(days=random.randint(0, 30))

            concluido = bool(random.randint(0, 1))

            criar_historico(username, midia.titulo, dataHistorico, concluido)

            count += 1
        else:
            break

def configurar_bd():
    criar_superuser('Gilmor', 'admin@example.com', '12345678', 'Gilmor', 'Gilmor')    

    criar_perfil_colaborador('Gilmor', 'masteruser', 'aprovado', True)
    
    criar_user('MarcosSerra', 'marquinhosserragens@gmail.com', 'senha_teste', 'Marcos', 'Serra')

    criar_bd_filmes()

    criar_atividade_user('MarcosSerra')

    #criar_perfil_colaborador('MarcosSerra', 'reportuser', 'analise', 'False')

    #criar_mensagem()

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