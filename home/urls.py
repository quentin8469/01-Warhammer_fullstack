from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import homeview

app_name = "home"

urlpatterns = [
    path("", homeview, name="acceuil"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
