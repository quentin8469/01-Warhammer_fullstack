from django import forms
from warhammer.models import (
    Campagne,
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
            "date_debut": forms.DateInput(attrs={"style": "width:15ch"}),
            "date_end": forms.DateInput(attrs={"style": "width:15ch"}),
        }
