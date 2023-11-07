from django.urls import path
from gestor.views import home, login, cadastro, user_menu


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('login/cadastro', cadastro, name='cadastro'),
    path('user/', user_menu, name='user_menu'),
]