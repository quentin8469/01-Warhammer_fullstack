from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from warhammer.views import WarhamCampaignListView


app_name = "warhammer"

urlpatterns = [
    path("", WarhamCampaignListView.as_view(), name="liste_campagne"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
