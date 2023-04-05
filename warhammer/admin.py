from django.contrib import admin
from warhammer.models import Campagne, Player

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


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nom",
        "race",
        "sexe",
        "vocation",
        "alignement",
        "age",
        "taille",
        "poids",
        "cheveux",
        "yeux",
        "photo_personnage",
        "point_destin",
        "debouches",
        "point_folie",
        "langue",
        "note",
        "mort_tuer",
        "date_creation",
        "date_update",
        "joueur",
        "campagne",
    )
