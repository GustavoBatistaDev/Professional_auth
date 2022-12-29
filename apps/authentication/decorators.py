from typing import Callable
from django.http import HttpRequest
from django.shortcuts import redirect
from django.http import HttpResponse


def not_authenticated(function: Callable, redirect_url:str='/'):
    def wrapper(request: HttpRequest):

        if request.user.is_authenticated:
            return redirect(redirect_url)

        return function(request)

    return wrapper







