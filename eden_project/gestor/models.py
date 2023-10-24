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
    descricao = models.TextField(default="Escreva sua descrição", max_length= 150, blank= True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='analise')
    dataPostagem = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='user_list', on_delete=models.CASCADE)
    ## cartas
    ## filme player

    def __str__(self):
        return self.titulo


class PerfilColaborador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ## cargos
    ## textoMotivacao
    ## status

    def __str__(self):
        return self.user
    

class UserRequestePerfilColaborador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    textoMotivacao = models.TextField(default="Porque você quer ser coloborador?", max_length= 150, blank= True)

    def __str__(self):
        return self.user

#class FomularioSuporte(models.Model):
#    user = models.ForeignKey(User, related_name='user_list', on_delete=models.CASCADE, blank= True, null= True)
#    titulo = models.CharField(max_length=100)
    ## status ou colaborador

#class MensagemFomularioSuporte(models.Model):
#    user = models.ForeignKey(User, related_name='user_list', on_delete=models.CASCADE, blank= True, null= True)
    ## mensagem
    ## dataMensagem
