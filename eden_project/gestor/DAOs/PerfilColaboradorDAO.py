from gestor.models import PerfilColaborador

def intancePerfilColaborador(user, cargo, motivacao,status , atividade):
    perfil, _ = PerfilColaborador.objects.get_or_create(user=user)

    perfil.cargo = cargo
    perfil.motivacao = motivacao
    perfil.status = status
    perfil.atividade = atividade

    perfil.save()

    return perfil


 