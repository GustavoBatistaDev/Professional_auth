from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm


def register(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        
        register_form = RegisterForm()

        return render(request, 'register.html', {'register_form': register_form})

    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            # todo redirecionar para login
            return HttpResponse('Salvo no banco com sucesso.')
        
        return render(request, 'register.html', {'register_form': register_form})

        

        
    

