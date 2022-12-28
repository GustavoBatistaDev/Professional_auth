from django import forms
from django.contrib.auth import forms 
from .models import Users


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users
        

class RegisterForm(UserCreationForm):
    '''Formulario para criacao de usuarios sem permissoes administrativas.'''
    class Meta(UserCreationForm.Meta):
        fields = ('first_name','email')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    
