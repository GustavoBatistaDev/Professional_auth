from django.urls import path
from . import views
from django.shortcuts import redirect
from django.urls import reverse


urlpatterns = [
    path('register/', views.register, name='register'),
    path('active_account/<uidb4>/<token>', views.active_account, name='active_account'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout')

]