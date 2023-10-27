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
    argMidia = models.ImageField(upload_to="arqmidia/%Y/%m/%d/", blank=True, null=True)
    arqCartaz = models.ImageField(upload_to="arqcartaz/%Y/%m/%d/", blank=True , null=True)

    def __str__(self):
        return self.titulo


class PerfilColaborador(models.Model):
    CARGO_CHOICES = (
        ('masteruser', 'MasterUser'),
        ('reportuser', 'ReportUser'),
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

