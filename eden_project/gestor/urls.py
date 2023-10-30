from django.urls import path
from gestor.views import home


urlpatterns = [
    path('', home, name='home'),
    
]