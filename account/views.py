from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class UserConnectionView(LoginView):
    template_name = "registration/login/connexion.html"
    redirect_authenticated_user = True


class UserInscriptionView:
    pass


class UserDeconnectionView(LogoutView):
    next_page = "account:connexion"
