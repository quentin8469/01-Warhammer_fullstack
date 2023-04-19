from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from account.forms import UserConnexionForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from account.forms import NewUserRegistrationForm

# Create your views here.


class UserConnectionView(LoginView):
    authentication_form = UserConnexionForm
    template_name = "accountTemplate/login/connexion.html"
    redirect_authenticated_user = True
    success_message = "Vous êtes connecté avec succès !"
    extra_context = {
        "titre": "Connexion",
        "slogan": "Connectez-vous pour accéder à votre compte.",
    }


class UserDeconnectionView(LogoutView):
    next_page = "account:connexion"


class UserInscriptionView(SuccessMessageMixin, CreateView):
    """Vue d'inscription personnalisée."""

    template_name = "accountTemplate/register/inscription.html"
    form_class = NewUserRegistrationForm
    success_url = reverse_lazy("home:acceuil")
    success_message = "Vous êtes inscrit avec succès !"
    extra_context = {
        "titre": "Inscription",
        "slogan": "Créez un nouveau compte pour accéder à toutes les fonctionnalités.",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def form_valid(self, form):
        """Surcharger la méthode form_valid pour connecter l'utilisateur automatiquement après une inscription réussie."""
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
