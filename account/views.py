from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.urls import reverse
from account.forms import NewUserRegistrationForm, UserConnexionForm, UserUpdateForm
from account.models import CustomUser

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


@method_decorator(login_required, name="dispatch")
class UserMonComptDetailsView(DetailView):
    """ """

    model = CustomUser
    template_name = "accountTemplate/details/user_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        utilisateur = CustomUser.objects.get(id=self.kwargs["pk"])
        context["utilisateur"] = utilisateur
        return super().get_context_data(**context)


@method_decorator(login_required, name="dispatch")
class UserMonComptDeleteViews(DeleteView):
    """Suppression d'un utilisateur"""

    model = CustomUser
    context_object_name = "user"
    template_name = "accountTemplate/delete/user_delete.html"
    success_url = "/account/connexion/"


@method_decorator(login_required, name="dispatch")
class UserMonComptUpdateView(UpdateView):
    """"""

    model = CustomUser
    form_class = UserUpdateForm
    template_name = "accountTemplate/update/user_update.html"

    def get_success_url(self):
        utilisateur = CustomUser.objects.get(id=self.kwargs["pk"])
        return reverse("account:monCompte", kwargs={"pk": utilisateur.id})
