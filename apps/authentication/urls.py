from django.urls import path
from . import views
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('active_account/<uidb4>/<token>', views.active_account, name='active_account'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="recuperar_senha/password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="recuperar_senha/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="recuperar_senha/password_reset_confirm_view.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="recuperar_senha/password_reset_complete.html"), name="password_reset_complete"),

]