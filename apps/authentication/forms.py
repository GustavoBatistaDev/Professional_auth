from django import forms as django_forms
from django.contrib.auth import forms, authenticate, login
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
        max_length = 245,
        widget = django_forms.EmailInput(attrs={'class': 'login__input', 'id': 'login-input-user'})
    )

    password = django_forms.CharField(
        label = 'Password',
        max_length= 245,
        strip= True,
        widget = django_forms.PasswordInput(attrs={'class': 'login__input'})
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

    def log_into(self, request):
        if not self.user:
            raise TypeError('self.user cannot be None, run form.is_valid() first')

        login(request, self.user)
        return self.user


    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code='invalid_login'
        )
    
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
            self.fields[field].widget.attrs.update({'class': 'login__input', 'id': 'login-input-user'})

    def clean_first_name(self) -> str:
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) <= 2:
            raise ValidationError('Primeiro nome precisar ter mais que 2 caracteres.')
        return super().clean_password2()

#   widget = django_forms.EmailInput(attrs={'class': 'login__input', 'id': 'login-input-user'})
    
