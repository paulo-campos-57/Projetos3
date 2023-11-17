from django import forms
from .models import PerfilColaborador, Mensagens, FormularioReporte
from django.forms import ModelForm

class PerfilColacoradorForm(ModelForm):
    cargo = forms.ChoiceField(
        choices=[
            ('reportuser', 'ReportUser'),
            ('midiauser', 'MidiaUser'),
        ],
        label="Cargo"
    )

    motivacao = forms.CharField(
        label="Motivação",  # Label que será exibido no formulário
        widget=forms.Textarea(attrs={'rows': 4}),  # Widget Textarea para permitir texto longo
        max_length=250,  # Máximo de 250 caracteres
        required=True  # Campo obrigatório
    )

    class Meta:
        model = PerfilColaborador
        fields = ['cargo', 'motivacao']

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