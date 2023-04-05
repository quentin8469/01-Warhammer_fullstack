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


class Player(models.Model):
    """ """

    CHOICE_RACE = {
        ("Nain", "Nain"),
        ("Elfe", "Elfe"),
        ("Humain", "Humain"),
        ("Halfeling", "Halfeling"),
    }

    CHOICE_SEXE = {
        ("Mâle", "Mâle"),
        ("Femelle", "Femelle"),
    }

    VOCATION_CHOICE = {
        ("Guerrier", "Guerrier"),
        ("Forestier", "Forestier"),
        ("Filou", "Filou"),
        ("Erudit", "Erudit"),
    }

    ALIGEMENT_CHOICE = {
        ("Loyal", "Loyal"),
        ("Bon", "Bon"),
        ("Neutre", "Neutre"),
        ("Mauvais", "Mauvais"),
        ("Chaotique", "Chaotique"),
    }

    nom = models.CharField(max_length=50, null=False)
    race = models.CharField(max_length=50, choices=CHOICE_RACE)
    sexe = models.CharField(max_length=50, choices=CHOICE_SEXE)
    vocation = models.CharField(max_length=50, choices=VOCATION_CHOICE)
    alignement = models.CharField(max_length=50, choices=ALIGEMENT_CHOICE)
    age = models.PositiveIntegerField(blank=True, null=True)
    taille = models.CharField(max_length=50, blank=True, null=True)
    poids = models.PositiveIntegerField(blank=True, null=True)
    cheveux = models.CharField(max_length=50, blank=True, null=True)
    yeux = models.CharField(max_length=50, blank=True, null=True)
    photo_personnage = models.ImageField(
        upload_to="photo_perso/", blank=True, null=True
    )
    point_destin = models.PositiveIntegerField(blank=True, null=True, default=0)
    debouches = models.TextField(blank=True, null=True)

    point_folie = models.PositiveIntegerField(blank=True, null=True, default=0)
    langue = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    mort_tuer = models.TextField(blank=True, null=True)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, blank=True)
    joueur = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    campagne = models.ForeignKey(
        to=Campagne, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return f"{self.nom} - {self.joueur}"
