from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account.views import (
    UserConnectionView,
    UserDeconnectionView,
    UserInscriptionView,
    UserMonComptDetailsView,
    UserMonComptDeleteViews,
    UserMonComptUpdateView,
)

app_name = "account"

urlpatterns = [
    path("connexion/", UserConnectionView.as_view(), name="connexion"),
    path("deconnexion/", UserDeconnectionView.as_view(), name="deconnexion"),
    path("inscription/", UserInscriptionView.as_view(), name="inscription"),
    path("monCompte/<int:pk>/", UserMonComptDetailsView.as_view(), name="monCompte"),
    path(
        "editterProfil/<int:pk>/",
        UserMonComptUpdateView.as_view(),
        name="editterProfil",
    ),
    path(
        "supprimerProfil/<int:pk>/",
        UserMonComptDeleteViews.as_view(),
        name="supprimerProfil",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
