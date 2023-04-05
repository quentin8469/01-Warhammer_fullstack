from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from warhammer.views import (
    WarhamCampaignListView,
    WarhamCampaignCreateView,
    WarhamCampagneUpdateView,
    WarhamCampagneDeleteViews,
)


app_name = "warhammer"

urlpatterns = [
    path("", WarhamCampaignListView.as_view(), name="liste_campagne"),
    path(
        "Creationcampagne/",
        WarhamCampaignCreateView.as_view(),
        name="creation_campagne",
    ),
    path(
        "edit_campagne/<int:pk>/",
        WarhamCampagneUpdateView.as_view(),
        name="editter_campagne",
    ),
    path(
        "campagne_delete/<int:pk>/",
        WarhamCampagneDeleteViews.as_view(),
        name="supprimer_campagne",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
