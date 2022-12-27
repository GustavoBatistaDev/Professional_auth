from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForms, UserCreationForm


@admin.register(Users)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForm
    model = Users
    list_display = ("email", "first_name", "last_name", "is_staff")
    fieldsets = auth_admin.UserAdmin.fieldsets + (

    )
