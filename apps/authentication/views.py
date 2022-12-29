from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm, AuthFormLogin
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import login as auth_login,logout
from django.urls import reverse
from .decorators import not_authenticated


#@not_authenticated
def register(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':

        register_form = RegisterForm()

        return render(request, 'register.html', {'register_form': register_form})

    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():

            new_form = register_form.save(commit=False)
            new_form.is_active = False
            new_form.save()

            messages.add_message(request, constants.SUCCESS, 'Check your email to verificated your account' ) 
            return redirect(reverse('login'))
        
        return render(request, 'register.html', {'register_form': register_form})

        
def active_account(request: HttpResponse, uidb4, token) -> HttpResponse:

    User = get_user_model()
    uid = force_str(urlsafe_base64_decode(uidb4))

    user = User.objects.filter(pk=uid)

    if (user := user.first()) and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        auth_login(request, user)

        messages.add_message(request, constants.SUCCESS, 'Your account has been saved successfully' ) 
        return redirect(reverse('login'))

    else:
        messages.add_message(request, constants.ERROR, 'The url accessed is not valid' ) 
        return redirect(reverse('register'))

#@not_authenticated
def login(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        auth_form_login = AuthFormLogin()
        return render(request, 'login.html', {'auth_form_login': auth_form_login})

    #elif request.method == 'POST':
      #  auth_form_login = AuthFormLogin(request.POST)

     #   if auth_form_login.is_valid():
        #    pass


def logout_user(request):
    logout(request)
    messages.add_message(request, constants.ERROR, 'you were logged out' )
    return redirect(reverse('login'))
   

    

        
    

