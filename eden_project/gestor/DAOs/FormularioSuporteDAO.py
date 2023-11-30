from gestor.models import FormularioSuporte

def getFormularioSuporteUser(user):
    suporte = FormularioSuporte.objects.filter(user=user)

    return suporte