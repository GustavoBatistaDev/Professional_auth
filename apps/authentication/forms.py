from django import forms as django_forms
from django.contrib.auth import forms, authenticate
from .models import Users
from django.core.exceptions import ValidationError


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users
        
class AuthFormLogin(django_forms.Form):
    email = django_forms.EmailField(
        label = "Email",
        max_length = 245,
        widget = django_forms.EmailInput(attrs={'class': 'form-control'})
    )

    password = django_forms.CharField(
        label = 'Password',
        max_length= 245,
        strip= True,
        widget = django_forms.PasswordInput(attrs={'class': 'form-control'})
    )

    error_messages = {
        'invalid_login': 'Invalid username or password',
        'inactive': 'User inactive '
    }

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        self.user = authenticate(username=email, password=password)

        if not self.user:
            raise self.get_invalid_login_error()

        else:
            self.confirm_user_activate()   


        return self.cleaned_data

    def get_invalid_login_error(self):
        return ValidationError(f'{self.error_messages["invalid_login"]}', code='invalid_login')
    
    def confirm_user_activate(self):
        if not self.user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive'
            )


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

    
