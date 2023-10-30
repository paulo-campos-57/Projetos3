from django.contrib import admin
from .models import PerfilColaborador, Midia, UserHistorico, Mensagens, FormularioReporte, FormularioSuporte,UserFeedback

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
    list_display = ("id", "user", "userDestino", "mensagem", "contexto", "dataMensagem")
    list_display_links = ("id", "user", "userDestino")
    search_fields = ("user__username", "contexto")

admin.site.register(Mensagens, ListandoMensagens)

class ListandoReportes(admin.ModelAdmin):
    list_display = ("user", "idFormulario", "texto", "arqMidia")
    list_display_links = ("texto",)
    search_fields = ("idFormulario",)

admin.site.register(FormularioReporte, ListandoReportes)

class ListandoSuportes(admin.ModelAdmin):
    list_display = ("id", "user", "texto")
    list_display_links = ("texto",)
    search_fields = ("user",)

admin.site.register(FormularioSuporte, ListandoSuportes)

class ListandoFeedback(admin.ModelAdmin):
    list_display = ("id", "user", "midia","comentario")
    list_display_links = ("midia",)
    search_fields = ("id",)

admin.site.register(UserFeedback,ListandoFeedback)