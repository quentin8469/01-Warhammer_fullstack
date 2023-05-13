from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cthulhu.views import cthulhuhomeview

app_name = "cthulhu"

urlpatterns = [
    path("", cthulhuhomeview, name="accueil"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
