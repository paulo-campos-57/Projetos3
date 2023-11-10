from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Midia(models.Model):
    STATUS_CHOICES = (
        ('analise', 'Em Análise'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    )

    titulo = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='user_list_midia', on_delete=models.CASCADE)
    descricao = models.TextField(default="Escreva sua descrição", max_length= 150, blank= False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='analise')
    dataPostagem = models.DateTimeField(auto_now_add=True)
    arqMidia = models.ImageField(upload_to="arqmidia/%Y/%m/%d/", blank=True, null=True) #tava argMidia, coloquei arqMidia
    arqCartaz = models.ImageField(upload_to="arqcartaz/%Y/%m/%d/", blank=True , null=True)

    def __str__(self):
        return self.titulo


class PerfilColaborador(models.Model):
    CARGO_CHOICES = (
        ('masteruser', 'MasterUser'),
        ('reportuser', 'ReportUser'), #nao seria mais adequado a nomenclatura dele ser "SuportUser"?
        ('midiauser', 'MidiaUser'),
    )

    STATUS_CHOICES = (
        ('analise', 'Em_Analise'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=10, choices=CARGO_CHOICES, default='midiauser')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='analise')
    atividade = models.BooleanField(default="False")

    def __str__(self):
        return self.user.username
    
class UserHistorico(models.Model):
    user = models.ForeignKey(User, related_name='user_list_historico', on_delete=models.CASCADE)
    midia = models.ForeignKey(Midia, related_name='midia_list_historico', on_delete=models.CASCADE)
    dataHustorico = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    concluido = models.BooleanField(default="False")

class Mensagens(models.Model):
    CONTEXTO_CHOICES = (
    ('notificacao', 'Notificacao'),
    ('pedido_de_cargo', 'Pedido_De_Cargo'),
    ('suporte', 'Suporte'),
    ('reportar', 'Reportar'),
    )
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_list_remetente', blank= False)
    userDestino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_list_destinatario', blank= False)
    mensagem = models.CharField(default="Escreva sua mensagem", max_length= 200, blank= False)
    contexto = models.CharField(max_length=15, choices=CONTEXTO_CHOICES, default='suporte', blank= False)
    dataMensagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensagem

class FormularioReporte(models.Model):
    REPORTE_CHOICES = (
        ('Conteudo_Inadequado', 'conteudo_inadequado'),
        ('Problema_de_Legenda ', 'problema_de_legenda'),
        ('Problema_de_Reproducao', 'problema_de_reproducao'),
        ('Outro', 'outro'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list_user_reporte', blank= False)
    categoriaReporte = models.CharField(max_length=23, choices=REPORTE_CHOICES, default='reporte', blank=False)
    midia = models.ForeignKey(Midia, related_name='midia_list_reporte', on_delete=models.CASCADE, blank=True, null=True)
    texto = models.CharField(default= "Descreva o problema encontrado", max_length=500, blank=False)

    def __str__(self):
        return self.texto

class FormularioSuporte(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_suporte', blank=False)
    texto = models.CharField(default="Informe a sua mensagem", max_length=500, blank=False)

    def __str__(self):
        return self.texto
    
class UserFeedback(models.Model):
    REACAO_CHOICES = (
    ('Like','like'),
    ('Dislike','dislike'),
    ('No_react','no_react'),
    )
    
    reacao = models.CharField(max_length=10, choices=REACAO_CHOICES, default='No_react', blank= False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_feedback', blank=False)
    midia = models.ForeignKey(Midia, related_name='midia_list_Feedback', on_delete=models.CASCADE)
    comentario = models.CharField(default="Traga o seu comentario", max_length=1000, blank=False)
    
    def __str__(self):
        return self.texto