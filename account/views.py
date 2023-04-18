from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from account.forms import UserConnexionForm

# Create your views here.


class UserConnectionView(LoginView):
    authentication_form = UserConnexionForm
    template_name = "accountTemplate/login/connexion.html"
    redirect_authenticated_user = True
    success_message = "Vous êtes connecté avec succès !"  # Message de succès affiché après une connexion réussie
    extra_context = {
        "titre": "Connexion",
        "slogan": "Connectez-vous pour accéder à votre compte.",
    }  # Contexte supplémentaire pour le modèle de template


class UserDeconnectionView(LogoutView):
    next_page = "account:connexion"


class UserInscriptionView:
    pass
