from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser


class NewUserRegistrationForm(UserCreationForm):
    """create a new user"""

    class Meta:
        """ """

        model = CustomUser
        fields = ("username", "email", "password1", "password2")
