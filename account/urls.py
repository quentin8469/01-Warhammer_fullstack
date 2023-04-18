from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account.views import UserConnectionView, UserDeconnectionView

app_name = "account"

urlpatterns = [
    path("connexion/", UserConnectionView.as_view(), name="connexion"),
    path("deconnexion/", UserDeconnectionView.as_view(), name="deconnexion"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
