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
    cargo = models.CharField(max_length=10, choices=CARGO_CHOICES, default='analise')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='analise')
    atividade = models.BooleanField(default="False")

    def __str__(self):
        return self.user.username
    
class UserHistorico(models.Model):
    user = models.ForeignKey(User, related_name='user_list_historico', on_delete=models.CASCADE)
    midia = models.ForeignKey(Midia, related_name='midia_list_historico', on_delete=models.CASCADE)
    concluido = models.BooleanField(default="False")

class Mensagens(models.Model):
    CONTEXTO_CHOICES = (
    ('notificacao', 'Notificacao'),
    ('pedido_de_cargo', 'Pedido_De_Cargo'),
    ('suporte', 'Suporte'),
    ('reportar', 'Reportar'),
    )
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_remetente', blank= False)
    userDestino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_destinatario', blank= False)
    mensagem = models.CharField(default="Escreva sua mensagem", max_length= 200, blank= False)
    idMensagem = models.AutoField(primary_key=True, editable=False)
    contexto = models.CharField(max_length=15, choices=CONTEXTO_CHOICES, default='suporte', blank= False)
    dataMensagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensagem

class FormularioReporte(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='midia', blank= False)
    texto = models.CharField(default= "Descreva o problema encontrado", max_length=500, blank=False)
    idFormulario = models.AutoField(primary_key=True, editable=False)
    arqMidia = models.ImageField(upload_to="arqmidia/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.texto