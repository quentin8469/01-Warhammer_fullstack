from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.models import CustomUser


class NewUserRegistrationForm(UserCreationForm):
    """create a new user"""

    class Meta:
        """ """

        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class UserConnexionForm(AuthenticationForm):
    """ """
    class Meta:
        model = CustomUser
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nom d'utilisateur"}
            ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Mot de passe"}
            ),
        }
        labels = {
            "username": "Nom d'utilisateur",
            "password": "Mot de passe",
        }
