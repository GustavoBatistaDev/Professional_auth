from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from django.http import HttpRequest, HttpResponse


def register(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        return render(request, 'register.html')

    
    #return HttpResponse('register')
    
    

