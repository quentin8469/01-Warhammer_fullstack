from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from warhammer.views import (
    WarhamCampaignListView,
    WarhamPlayerDetailView,
    WarhamCampaignCreateView,
    WarhamCampagneUpdateView,
    WarhamCampagneDeleteViews,
    WarhamCampaignPlayerListView,
    WarhamPlayerDeleteViews,
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
    path(
        "campagne/<int:pk>/",
        WarhamCampaignPlayerListView.as_view(),
        name="liste_personnages",
    ),
    path(
        "player/<int:pk>/",
        WarhamPlayerDetailView.as_view(),
        name="details_personnages",
    ),
    path(
        "player_delete/<int:pk>/",
        WarhamPlayerDeleteViews.as_view(),
        name="supprimer_personnages",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
