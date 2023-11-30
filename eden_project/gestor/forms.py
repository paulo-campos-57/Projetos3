from django import forms
from .models import PerfilColaborador, Mensagens, FormularioReporte
from django.forms import ModelForm

from django import forms

class PerfilColacoradorForm(forms.ModelForm):
    class Meta:
        model = PerfilColaborador
        fields = ['cargo', 'motivacao']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            # Se houver uma instância, preencha os campos com os valores do banco de dados
            initial = kwargs.get('initial', {})
            initial['cargo'] = instance.cargo
            initial['motivacao'] = instance.motivacao
            kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

class PerfilColacoradorFormChamar(forms.ModelForm):
    class Meta:
        model = PerfilColaborador
        fields = ['cargo']


class MensagensForm(ModelForm):
    class Meta:
        model = Mensagens
        fields = ('userDestino', 'mensagem', 'contexto')
# user
# userDestino
# mensagem
# contexto
# dataMensagem

class FormularioReporteForm(ModelForm):
    class Meta:
        model = FormularioReporte
        fields = ('user', 'categoriaReporte', 'midia', 'texto', 'status')
        
# user
# categoriaReporte
# midia
# texto
# status