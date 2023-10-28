from django.contrib import admin
from .models import PerfilColaborador, Midia, UserHistorico, Mensagens

# Register your models here.
class ListandoMidia(admin.ModelAdmin):
    list_display = ("id", "titulo", "user", "status", "dataPostagem")
    list_display_links =("id", "titulo")
    search_fields = ("titulo", "user",)

admin.site.register(Midia, ListandoMidia)

class ListandoPerfilColaborador(admin.ModelAdmin):
    list_display = ("id", "user", "cargo", "status","atividade")
    list_display_links =("id", "user")
    search_fields = ("user",)

admin.site.register(PerfilColaborador, ListandoPerfilColaborador)

class ListandoUserHistorico(admin.ModelAdmin):
    list_display = ("id", "user", "midia", "concluido")
    list_display_links = ("id", "user")
    search_fields = ("user",)

admin.site.register(UserHistorico, ListandoUserHistorico)

class ListandoMensagens(admin.ModelAdmin):
    list_display = ("user", "userDestino", "mensagem", "idMensagem", "contexto", "dataMensagem")
    list_display_links = ("user", "userDestino")
    search_fields = ("user__username", "contexto")

admin.site.register(Mensagens, ListandoMensagens)