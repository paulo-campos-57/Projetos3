from gestor.models import PerfilColaborador

def intancePerfilColaborador(user, cargo, status, atividade):
    perfil, _ = PerfilColaborador.objects.get_or_create(user=user)

    perfil.cargo = cargo
    perfil.status = status
    perfil.atividade = atividade

    perfil.save()

    return perfil


 