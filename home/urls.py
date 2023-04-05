from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import homeview

app_name= "home"

urlpatterns = [
    path("", homeview, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
