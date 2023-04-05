from django import forms
from warhammer.models import Campagne, Player

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
            "date_debut": forms.DateInput(attrs={"style": "width:15ch"}),
            "date_end": forms.DateInput(attrs={"style": "width:15ch"}),
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
