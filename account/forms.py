from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.models import CustomUser


class NewUserRegistrationForm(UserCreationForm):
    """Formulaire d'inscription pour créer un nouvel utilisateur."""

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nom d'utilisateur"}
            ),
            "password1": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Mot de passe"}
            ),
            "password2": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Répéter Mot de passe"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Votre email"}
            ),
        }
        labels = {
            "username": "Nom d'utilisateur",
            "email": "Email",
            "password1": "Mot de passe",
            "password2": "Répéter Mot de passe",
        }


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


class UserUpdateForm(forms.ModelForm):
    """"""

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
        ]
