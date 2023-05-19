from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cthulhu.views import CthulhuCampaignListView, CthulhuInvestigateurDetailView

app_name = "cthulhu"

urlpatterns = [
    #### camapgne url ####
    path("", CthulhuCampaignListView.as_view(), name="accueil"),
    #### investigateur url ####
    path(
        "investigateur/<int:pk>/",
        CthulhuInvestigateurDetailView.as_view(),
        name="details_investigateur",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
