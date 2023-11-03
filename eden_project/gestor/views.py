from django.shortcuts import render

# Create your views here.

def home(request):
    request.use=None
    return render(request, 'home.html')

def login(request):
    request.use=None
    return render(request, 'login.html')