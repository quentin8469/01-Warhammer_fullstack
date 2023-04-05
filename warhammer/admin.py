from django.contrib import admin
from warhammer.models import Campagne

# Register your models here.


@admin.register(Campagne)
class CampagneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nom_de_campagne",
        "date_creation",
        "date_update",
        "date_debut",
        "date_end",
        "image_campagne",
        "maitre_du_jeu",
        "campagne_etat",
    )
