from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm

@login_required(login_url='login')
def registerPage(request):
    form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Usuário cadastrado com sucesso.')
            form.save

    context = {'form': form}

    return render(request, 'accounts/register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('CPF')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'accounts/home.html')
        else:
            messages.info(request, 'CPF ou senha incorreta!' )
    context = {}
    return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html')

