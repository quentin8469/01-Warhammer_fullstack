from django import forms
from django.contrib.admin import widgets
from warhammer.models import (
    Campagne,
    Player,
    PointDeBlessure,
    PointDeDestin,
    PlanCarriere,
    Equipement,
    ExperiencePersonnage,
    DescriptionPersonnelle,
    CaracteristiqueActuelle,
    CaracteristiqueBase,
    ArmeContact,
    ArmeDistance,
    Armure,
    Bourse,
    Magie,
    Monture,
    Sortilege,
    Competence,
)

# form 15
class NewWarhammerCampagneForm(forms.ModelForm):
    """"""

    class Meta:
        model = Campagne
        fields = [
            "nom_de_campagne",
            "image_campagne",
            "maitre_du_jeu",
            "campagne_etat",
            "date_debut",
            "date_end",
        ]
        widgets = {
            "date_debut": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd (DOB)",
                    "style": "width:15ch",
                }
            ),
            "date_end": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd (DOB)",
                    "style": "width:15ch",
                }
            ),
        }


# form1
class NewWarhammerPlayerForm(forms.ModelForm):
    """Player form to create a new warhammer player"""

    class Meta:
        model = Player
        fields = [
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
            "campagne",
        ]
        widgets = {
            "poids": forms.NumberInput(attrs={"style": "width:15ch"}),
            "age": forms.NumberInput(attrs={"style": "width:15ch"}),
            "campagne": forms.Select(choices=Campagne.objects.all()),
        }


# form2
class NewCaracteristiqueBaseForm(forms.ModelForm):
    """"""

    class Meta:
        model = CaracteristiqueBase
        fields = [
            "mouvement",
            "capacite_combat",
            "capacité_tir",
            "force",
            "endurance",
            "point_blessure",
            "initiative",
            "nb_attaque",
            "dexterite",
            "commandement",
            "intelligence",
            "calme",
            "force_mentale",
            "sociabilite",
        ]
        widgets = {
            "mouvement": forms.NumberInput(attrs={"style": "width:6ch"}),
            "capacite_combat": forms.NumberInput(attrs={"style": "width:6ch"}),
            "capacité_tir": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force": forms.NumberInput(attrs={"style": "width:6ch"}),
            "endurance": forms.NumberInput(attrs={"style": "width:6ch"}),
            "point_blessure": forms.NumberInput(attrs={"style": "width:6ch"}),
            "initiative": forms.NumberInput(attrs={"style": "width:6ch"}),
            "nb_attaque": forms.NumberInput(attrs={"style": "width:6ch"}),
            "dexterite": forms.NumberInput(attrs={"style": "width:6ch"}),
            "commandement": forms.NumberInput(attrs={"style": "width:6ch"}),
            "intelligence": forms.NumberInput(attrs={"style": "width:6ch"}),
            "calme": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force_mentale": forms.NumberInput(attrs={"style": "width:6ch"}),
            "sociabilite": forms.NumberInput(attrs={"style": "width:6ch"}),
        }


# form3
class NewPlanCarriereForm(forms.ModelForm):
    """"""

    class Meta:
        model = PlanCarriere
        fields = [
            "nom",
            "mouvement",
            "capacite_combat",
            "capacité_tir",
            "force",
            "endurance",
            "point_blessure",
            "initiative",
            "nb_attaque",
            "dexterite",
            "commandement",
            "intelligence",
            "calme",
            "force_mentale",
            "sociabilite",
        ]
        widgets = {
            "mouvement": forms.NumberInput(attrs={"style": "width:6ch"}),
            "capacite_combat": forms.NumberInput(attrs={"style": "width:6ch"}),
            "capacité_tir": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force": forms.NumberInput(attrs={"style": "width:6ch"}),
            "endurance": forms.NumberInput(attrs={"style": "width:6ch"}),
            "point_blessure": forms.NumberInput(attrs={"style": "width:6ch"}),
            "initiative": forms.NumberInput(attrs={"style": "width:6ch"}),
            "nb_attaque": forms.NumberInput(attrs={"style": "width:6ch"}),
            "dexterite": forms.NumberInput(attrs={"style": "width:6ch"}),
            "commandement": forms.NumberInput(attrs={"style": "width:6ch"}),
            "intelligence": forms.NumberInput(attrs={"style": "width:6ch"}),
            "calme": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force_mentale": forms.NumberInput(attrs={"style": "width:6ch"}),
            "sociabilite": forms.NumberInput(attrs={"style": "width:6ch"}),
        }


# form4
class NewCaracteristiqueActuelleForm(forms.ModelForm):
    """"""

    class Meta:
        model = CaracteristiqueActuelle
        fields = [
            "mouvement",
            "capacite_combat",
            "capacité_tir",
            "force",
            "endurance",
            "point_blessure",
            "initiative",
            "nb_attaque",
            "dexterite",
            "commandement",
            "intelligence",
            "calme",
            "force_mentale",
            "sociabilite",
        ]
        widgets = {
            "mouvement": forms.NumberInput(attrs={"style": "width:6ch"}),
            "capacite_combat": forms.NumberInput(attrs={"style": "width:6ch"}),
            "capacité_tir": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force": forms.NumberInput(attrs={"style": "width:6ch"}),
            "endurance": forms.NumberInput(attrs={"style": "width:6ch"}),
            "point_blessure": forms.NumberInput(attrs={"style": "width:6ch"}),
            "initiative": forms.NumberInput(attrs={"style": "width:6ch"}),
            "nb_attaque": forms.NumberInput(attrs={"style": "width:6ch"}),
            "dexterite": forms.NumberInput(attrs={"style": "width:6ch"}),
            "commandement": forms.NumberInput(attrs={"style": "width:6ch"}),
            "intelligence": forms.NumberInput(attrs={"style": "width:6ch"}),
            "calme": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force_mentale": forms.NumberInput(attrs={"style": "width:6ch"}),
            "sociabilite": forms.NumberInput(attrs={"style": "width:6ch"}),
        }


# form5
class NewCompetenceForm(forms.ModelForm):
    """"""

    class Meta:
        model = Competence
        fields = [
            "nom",
            "description",
            "bonus",
            "malus",
            "apprentissage",
            "cout_xp",
            "niveau",
        ]


# form7
class NewDescriptionPersonnelleForm(forms.ModelForm):
    """"""

    class Meta:
        model = DescriptionPersonnelle
        fields = [
            "lieu_naissance",
            "signe_distinctif",
            "Membre_famille",
            "description_perso",
        ]


# form8
class NewArmeContactForm(forms.ModelForm):
    """"""

    class Meta:
        model = ArmeContact
        fields = [
            "nom",
            "initiative",
            "toucher",
            "degats",
            "parade",
            "degats",
            "parade",
            "encombrement",
            "note",
        ]
        widgets = {
            "nom": forms.TextInput(attrs={"size": "20"}),
            "initiative": forms.NumberInput(attrs={"style": "width:6ch"}),
            "toucher": forms.NumberInput(attrs={"style": "width:6ch"}),
            "degats": forms.NumberInput(attrs={"style": "width:6ch"}),
            "parade": forms.NumberInput(attrs={"style": "width:6ch"}),
            "encombrement": forms.NumberInput(attrs={"style": "width:6ch"}),
        }


# form9
class NewArmeDistanceForm(forms.ModelForm):
    """"""

    class Meta:
        model = ArmeDistance
        fields = [
            "nom",
            "porte_courte",
            "porte_longue",
            "porte_extreme",
            "force_effective",
            "armer_tirer",
            "encombrement",
            "munitions",
            "nb_munitions",
            "note",
        ]
        widgets = {
            "nom": forms.TextInput(attrs={"size": "14"}),
            "porte_courte": forms.NumberInput(attrs={"style": "width:6ch"}),
            "porte_longue": forms.NumberInput(attrs={"style": "width:6ch"}),
            "porte_extreme": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force_effective": forms.NumberInput(attrs={"style": "width:6ch"}),
            "armer_tirer": forms.TextInput(attrs={"size": "6"}),
            "encombrement": forms.NumberInput(attrs={"style": "width:6ch"}),
        }


# form 10
class NewArmureForm(forms.ModelForm):
    """"""

    class Meta:
        model = Armure
        fields = [
            "nom",
            "protection",
            "localisation",
            "encombrement",
            "note",
        ]
        widgets = {
            "protection": forms.NumberInput(attrs={"style": "width:10ch"}),
            "encombrement": forms.NumberInput(attrs={"style": "width:10ch"}),
        }


# form 11
class NewMagieForm(forms.ModelForm):
    """"""

    class Meta:
        model = Magie
        fields = [
            "point_magie_personnage",
            "point_magie_actuel",
            "point_magie_supplementaire",
            "famillier_personnage",
            "nombre_sort",
            "recuperation_pm",
            "armure_autorisee",
            "arme_non_autorisee",
            "niveau_magique",
            "niveau_pouvoir",
            "note",
        ]


# form6
class NewEquipementForm(forms.ModelForm):
    """"""

    class Meta:
        model = Equipement
        fields = ["nom", "quantite", "encombrement", "note"]
        widgets = {
            "quantite": forms.NumberInput(attrs={"style": "width:15ch"}),
            "encombrement": forms.NumberInput(attrs={"style": "width:15ch"}),
        }


# form 12
class NewBourseForm(forms.ModelForm):
    """"""

    class Meta:
        model = Bourse
        fields = ["couronne", "pistole", "sous", "encombrement", "autre"]


# form 13
class NewMontureForm(forms.ModelForm):
    """"""

    class Meta:
        model = Monture
        fields = [
            "nom",
            "mouvement",
            "capacite_combat",
            "capacité_tir",
            "force",
            "endurance",
            "point_blessure",
            "initiative",
            "nb_attaque",
            "dexterite",
            "commandement",
            "intelligence",
            "calme",
            "force_mentale",
            "sociabilite",
        ]
        widgets = {
            "mouvement": forms.NumberInput(attrs={"style": "width:6ch"}),
            "capacite_combat": forms.NumberInput(attrs={"style": "width:6ch"}),
            "capacité_tir": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force": forms.NumberInput(attrs={"style": "width:6ch"}),
            "endurance": forms.NumberInput(attrs={"style": "width:6ch"}),
            "point_blessure": forms.NumberInput(attrs={"style": "width:6ch"}),
            "initiative": forms.NumberInput(attrs={"style": "width:6ch"}),
            "nb_attaque": forms.NumberInput(attrs={"style": "width:6ch"}),
            "dexterite": forms.NumberInput(attrs={"style": "width:6ch"}),
            "commandement": forms.NumberInput(attrs={"style": "width:6ch"}),
            "intelligence": forms.NumberInput(attrs={"style": "width:6ch"}),
            "calme": forms.NumberInput(attrs={"style": "width:6ch"}),
            "force_mentale": forms.NumberInput(attrs={"style": "width:6ch"}),
            "sociabilite": forms.NumberInput(attrs={"style": "width:6ch"}),
        }


# form 14
class NewExperiencePersonnageForm(forms.ModelForm):
    """"""

    class Meta:
        model = ExperiencePersonnage
        fields = ["xp_actuelle", "xp_depense"]


# form 16
class NewPointDeBlessureForm(forms.ModelForm):
    """"""

    class Meta:
        model = PointDeBlessure
        fields = ["pdb_max", "pdb_actuel", "nb_blessure"]
        widgets = {
            "pdb_max": forms.NumberInput(attrs={"style": "width:10ch"}),
            "pdb_actuel": forms.NumberInput(attrs={"style": "width:10ch"}),
            "nb_blessure": forms.NumberInput(attrs={"style": "width:10ch"}),
        }


# form 17
class NewPointDeDestinForm(forms.ModelForm):
    """"""

    class Meta:
        model = PointDeDestin
        fields = ["pdd_actuel", "pdd_depense"]
        widgets = {
            "pdd_actuel": forms.NumberInput(attrs={"style": "width:10ch"}),
            "pdd_depense": forms.NumberInput(attrs={"style": "width:10ch"}),
        }


# from 18
class NewSortilegeForm(forms.ModelForm):
    """"""

    class Meta:
        model = Sortilege
        fields = [
            "nom_sortilege",
            "type_magie",
            "niveau_sort",
            "cout_point_magie",
            "porte",
            "duree",
            "degats",
            "composants",
            "description_sort",
            "incantation",
            "apprentissage",
            "cout_xp",
            "note",
        ]
