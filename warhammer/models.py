from django.db import models
from account.models import CustomUser


class Campagne(models.Model):
    """Create the game campaign"""

    ETAT_CAMPAGNE = {
        ("En cours", "En cours"),
        ("En pause", "En pause"),
        ("Terminée", "Terminée"),
    }

    nom_de_campagne = models.CharField(max_length=150, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, blank=True)
    date_debut = models.DateField(blank=True)
    date_end = models.DateField(null=True, blank=True)
    image_campagne = models.ImageField(
        upload_to="image_campagne/", blank=True, null=True
    )
    campagne_etat = models.CharField(max_length=20, choices=ETAT_CAMPAGNE)
    maitre_du_jeu = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Campagne"
        verbose_name_plural = "Campagnes"

    def __str__(self):
        return f"{self.nom_de_campagne} - {self.maitre_du_jeu}"
