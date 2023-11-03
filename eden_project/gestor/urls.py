from django.urls import path
from gestor.views import home, login, cadastro


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('login/cadastro', cadastro, name='cadastro'),
]