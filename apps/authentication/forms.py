from django import forms
from django.contrib.auth import forms
from .models import Users


class UserChangeForms(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users


class UserCreationForm(forms.UserChangeForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users