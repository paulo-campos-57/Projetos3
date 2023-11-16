from django import forms
from django.forms import ModelForm
from .models import Mensagens, FormularioReporte

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