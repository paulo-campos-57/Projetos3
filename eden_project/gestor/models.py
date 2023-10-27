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
    user = models.ForeignKey(User, related_name='user_list', on_delete=models.CASCADE)
    descricao = models.TextField(default="Escreva sua descrição", max_length= 150, blank= True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='analise')
    dataPostagem = models.DateTimeField(auto_now_add=True)
    ## argMidia
    ## arqCartaz

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
    cargo = models.CharField(max_length=10, choices=STATUS_CHOICES, default='analise')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='analise')
    atividade = models.BooleanField(default="True")

    def __str__(self):
        return self.user