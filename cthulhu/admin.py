from django.contrib import admin
from cthulhu.models import (
    CampagneCthulhu,
    Investigateur,
    Caracteristique,
    CompetenceInvestigateur,
    Armes,
)


# Register your models here.
@admin.register(CampagneCthulhu)
class CampagneCthulhuAdmin(admin.ModelAdmin):
    list_display = (
        "style_de_jeu",
        "nom_de_campagne",
        "date_creation",
        "date_update",
        "date_debut",
        "date_end",
        "image_campagne",
        "campagne_etat",
        "gardien",
    )


@admin.register(Investigateur)
class InvestigateurAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "prenom",
        "occupation",
        "age",
        "sexe",
        "profession",
        "nationalite",
        "personnalite",
        "photo_investigateur",
        "description",
        "cercle_proche",
        "cercle_eloigner",
        "cercle_opposer",
        "cercle_ennemis",
        "etat_investigateur",
        "date_creation",
        "date_update",
        "joueur",
        "campagne_cthulhu",
    )


@admin.register(Caracteristique)
class CaracteristiqueAdmin(admin.ModelAdmin):
    list_display = (
        "apparence",
        "constitution",
        "dexterite",
        "force",
        "taille",
        "education",
        "intelligence",
        "pouvoir",
        "aplomb",
        "prestance",
        "endurance",
        "agilte",
        "puissance",
        "corpulence",
        "connaissance",
        "intuition",
        "volonte",
        "sante_mentale",
        "points_de_vie",
        "seuil_de_blessure",
        "point_de_magie",
        "impact",
    )


@admin.register(CompetenceInvestigateur)
class CompetenceInvestigateurAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "category",
        "description",
        "niveau_naturel",
        "point_ajouter",
        "tirage_xp",
        "is_occupation",
        "investigateur",
        "total_pourcentage_competence",
    )


@admin.register(Armes)
class ArmesAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "nom",
        "modificateur",
        "dommage",
        "portee",
        "cadence",
        "munition",
        "investigateur",
    )
