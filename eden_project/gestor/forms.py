from django import forms
from .models import PerfilColaborador, Mensagens, FormularioReporte
from django.forms import ModelForm

class PerfilColacoradorForm(ModelForm):
    class Meta:
        model = PerfilColaborador
        fields = ['cargo']

        CARGO_CHOICES = [
            ('reportuser', 'ReportUser'), 
            ('midiauser', 'MidiaUser'),
        ]

        cargo = forms.ChoiceField(choices=CARGO_CHOICES)

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