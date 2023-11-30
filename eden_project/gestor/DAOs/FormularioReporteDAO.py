from gestor.models import FormularioReporte

def getFormularioReporteUser(user):
    reporte = FormularioReporte.objects.filter(user=user)

    return reporte