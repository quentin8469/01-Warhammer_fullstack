import math
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    FileExtensionValidator,
)
from PIL import Image
from account.models import CustomUser


# Create your models here.
class CampagneCthulhu(models.Model):
    """Create the game campaign"""

    ETAT_CAMPAGNE = {
        ("En cours", "En cours"),
        ("En pause", "En pause"),
        ("Terminée", "Terminée"),
    }
    CHOICE_STYLE = {
        ("Horreur Lovecraftienne", "Horreur Lovecraftienne"),
        ("Investigation Occulte", "Investigation Occulte"),
        ("Aventure Pulp", "Aventure Pulp"),
    }
    style_de_jeu = models.CharField(max_length=50, choices=CHOICE_STYLE)
    nom_de_campagne = models.CharField(max_length=150, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    image_campagne = models.ImageField(
        upload_to="image_campagne/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
        ],
    )
    campagne_etat = models.CharField(max_length=20, choices=ETAT_CAMPAGNE)
    gardien = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Campagne"
        verbose_name_plural = "Campagnes"
        ordering = ["campagne_etat"]

    def __str__(self):
        return f"{self.nom_de_campagne} - {self.gardien}"

    # @classmethod
    # def validate_image_size_and_file_size(cls, image_campagne):
    #     max_width = 1200
    #     max_height = 800
    #     max_file_size = 2 * 1024 * 1024  # 2 Mo

    #     # Vérification de la taille de l'image
    #     image_campagne = Image.open(image_campagne)
    #     width, height = image_campagne.size
    #     if width > max_width or height > max_height:
    #         raise ValidationError(
    #             "La taille de l'image ne doit pas dépasser {} pixels de largeur et {} pixels de hauteur.".format(
    #                 max_width, max_height
    #             )
    #         )

    #     # Vérification de la taille du fichier
    #     if image_campagne.size > max_file_size:
    #         raise ValidationError("La taille de l'image ne doit pas dépasser 2 Mo.")

    # def clean(self):
    #     super().clean()
    #     self.validate_image_size_and_file_size(self.image_campagne)


class Investigateur(models.Model):
    """Class pour créer un investigateur Cthulhu"""

    CHOICE_SEXE = {
        ("Mâle", "Mâle"),
        ("Femelle", "Femelle"),
    }

    ETAT_INVESTIGATEUR = {
        ("Actif", "Actif"),
        ("En pause", "En pause"),
        ("Fou", "Fou"),
        ("Mort", "Mort"),
        ("Avec Cthulhu", "Avec Cthulhu"),
    }
    CHOICE_OCCUPATION = {
        ("Artiste", "Artiste"),
        ("Baroudeur", "Baroudeur"),
        ("Détective", "Détective"),
        ("Dilettante", "Dilettante"),
        ("Explorateur", "Explorateur"),
        ("Homme de foi", "Homme de foi"),
        ("Journaliste", "Journaliste"),
        ("Médecin", "Médecin"),
        ("Militaire", "Militaire"),
        ("Universitaire", "Universitaire"),
    }
    CHOICE_PERSONNALITE = {
        ("Anxieux", "Anxieux"),
        ("Flegmatique", "Flegmatique"),
        ("Jovial", "Jovial"),
        ("Méfiant", "Méfiant"),
        ("Narcissique", "Narcissique"),
        ("Obsessionnel", "Obsessionnel"),
        ("Sanguin", "Sanguin"),
        ("Taciturne", "Taciturne"),
        ("Tatillon", "Tatillon"),
        ("Timide", "Timide"),
    }
    CHOICE_NIVEAU_VIE = {
        ("Indigent (5%)", "Indigent (5%)"),
        ("Pauvre (25%)", "Pauvre (25%)"),
        ("Classe moyenne (50%)", "Classe moyenne (50%)"),
        ("Aisée (75%)", "Aisée (75%)"),
        ("Riche (95%)", "Riche (95%)"),
    }

    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
    occupation = models.CharField(max_length=50, choices=CHOICE_OCCUPATION)
    age = models.PositiveIntegerField(blank=True, null=True, default=0)
    sexe = models.CharField(max_length=50, choices=CHOICE_SEXE)
    profession = models.CharField(max_length=50, null=False)
    nationalite = models.CharField(max_length=50, null=False)
    personnalite = models.CharField(max_length=50, choices=CHOICE_PERSONNALITE)
    photo_investigateur = models.ImageField(
        upload_to="photo_perso/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
        ],
    )
    description = models.TextField(blank=True, null=True)
    histoire_perso = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    blessure = models.TextField(blank=True, null=True)
    protection = models.TextField(blank=True, null=True)
    cercle_proche = models.CharField(max_length=50, null=False)
    cercle_eloigner = models.CharField(max_length=50, null=False)
    cercle_opposer = models.CharField(max_length=50, null=False)
    cercle_ennemis = models.CharField(max_length=50, null=False)
    etat_investigateur = models.CharField(max_length=20, choices=ETAT_INVESTIGATEUR)
    niveau_vie = models.CharField(max_length=20, choices=CHOICE_NIVEAU_VIE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, blank=True)
    joueur = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    campagne_cthulhu = models.ForeignKey(
        to=CampagneCthulhu, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "Investigateur"
        verbose_name_plural = "Investigateurs"

    def __str__(self):
        return f"{self.nom} - {self.joueur}"

    # @classmethod
    # def validate_image_size_and_file_size(cls, image):
    #     max_width = 1200
    #     max_height = 800
    #     max_file_size = 2 * 1024 * 1024  # 2 Mo

    #     # Vérification de la taille de l'image
    #     img = Image.open(image)
    #     width, height = img.size
    #     if width > max_width or height > max_height:
    #         raise ValidationError(
    #             "La taille de l'image ne doit pas dépasser {} pixels de largeur et {} pixels de hauteur.".format(
    #                 max_width, max_height
    #             )
    #         )

    #     # Vérification de la taille du fichier
    #     if image.size > max_file_size:
    #         raise ValidationError("La taille de l'image ne doit pas dépasser 2 Mo.")

    # def clean(self):
    #     super().clean()
    #     self.validate_image_size_and_file_size(self.image)


class Caracteristique(models.Model):
    """Classe de gestion des caracteristiques et attributs des joueurs"""

    apparence = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    constitution = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    dexterite = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    force = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    taille = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    education = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    intelligence = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    pouvoir = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    aplomb = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    investigateur = models.ForeignKey(to=Investigateur, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Caracteristique"
        verbose_name_plural = "Caracteristiques"

    def __str__(self):
        return f"{self.investigateur.nom} - {self.investigateur.joueur.username}"

    def prestance(self):
        prestance = self.apparence * 5
        return prestance

    def endurance(self):
        endurance = self.constitution * 5
        return endurance

    def agilte(self):
        agilte = self.dexterite * 5
        return agilte

    def puissance(self):
        puissance = self.force * 5
        return puissance

    def corpulence(self):
        corpulence = self.taille * 5
        return corpulence

    def connaissance(self):
        connaissance = self.education * 5
        return connaissance

    def intuition(self):
        intuition = self.intelligence * 5
        return intuition

    def volonte(self):
        volonte = self.pouvoir * 5
        return volonte

    def sante_mentale(self):
        sante_mentale = self.pouvoir * 5
        return sante_mentale

    def points_de_vie(self):
        points_de_vie = math.ceil((self.constitution + self.taille) / 2)
        return points_de_vie

    def seuil_de_blessure(self):
        pv = self.points_de_vie()
        seuil_de_blessure = math.floor((pv / 2))
        return seuil_de_blessure

    def point_de_magie(self):
        point_de_magie = self.pouvoir
        return point_de_magie

    def impact(self):
        impact = self.force + self.taille
        if 0 <= impact <= 12:
            return -4
        if 13 <= impact <= 16:
            return -2
        if 17 <= impact <= 24:
            return 0
        if 25 <= impact <= 32:
            return 2
        if 33 <= impact <= 40:
            return 4


class CompetenceInvestigateur(models.Model):
    """"""

    CATEGORY_CHOICE = {
        ("Connaissance", "Connaissance"),
        ("Savoir-faire", "Savoir-faire"),
        ("Sensorielle", "Sensorielle"),
        ("Influence", "Influence"),
        ("Action", "Action"),
    }
    nom = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICE)
    description = models.TextField(blank=True, null=True)
    niveau_naturel = models.PositiveIntegerField(
        default=00, validators=[MinValueValidator(00), MaxValueValidator(120)]
    )
    point_ajouter = models.PositiveIntegerField(
        default=00, validators=[MinValueValidator(00), MaxValueValidator(120)]
    )
    tirage_xp = models.BooleanField(default=False)
    is_occupation = models.BooleanField(default=False)
    investigateur = models.ForeignKey(to=Investigateur, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Competence Investigateur"
        verbose_name_plural = "Competences Investigateurs"

    def __str__(self):
        return f"{self.nom} - {self.investigateur.joueur.username}"

    def total_pourcentage_competence(self):
        if self.point_ajouter > 0:
            total = self.niveau_naturel + self.point_ajouter
            return total
        return self.niveau_naturel


class Armes(models.Model):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    CHOICE_TYPE = {
        ("Armes improvisées", "Armes improvisées"),
        ("Armes à Feu", "Arme à Feu"),
        ("Armes blanches", "Armes blanches"),
        ("Explosifs", "Explosifs"),
    }

    CHOICE_PORTEE = {
        ("Contact", "Contact"),
        ("Courte", "Courte"),
        ("Proche", "Proche"),
        ("Longue", "Longue"),
    }
    type = models.CharField(max_length=20, choices=CHOICE_TYPE)
    nom = models.CharField(max_length=50, null=False)
    modificateur = models.CharField(max_length=50, null=False)
    dommage = models.CharField(max_length=5, null=False)
    portee = models.CharField(max_length=20, choices=CHOICE_PORTEE)
    cadence = models.CharField(
        max_length=50, null=False, default="nombre de tir par round à definir"
    )
    munition = models.PositiveIntegerField(
        default=00, validators=[MinValueValidator(00), MaxValueValidator(120)]
    )
    description = models.TextField(blank=True, null=True)
    investigateur = models.ForeignKey(to=Investigateur, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Arme à Feu"
        verbose_name_plural = "Armes à Feu"

    def __str__(self):
        return f"{self.nom} - {self.investigateur.joueur.username}"


class SequellePsycologique(models.Model):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    nom = models.CharField(max_length=50, null=False)
    niveau = models.CharField(max_length=50, null=False)
    effet = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    investigateur = models.ForeignKey(to=Investigateur, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sequelle Psycologique"
        verbose_name_plural = "Sequelles Psycologiques"

    def __str__(self):
        return f"{self.nom} - {self.investigateur.joueur.username}"


class SequellePhysique(models.Model):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    nom = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    investigateur = models.ForeignKey(to=Investigateur, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sequelle Physique"
        verbose_name_plural = "Sequelles Physiques"

    def __str__(self):
        return f"{self.nom} - {self.investigateur.joueur.username}"


class Contact(models.Model):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    nom = models.CharField(max_length=50, null=False)
    attitude = models.CharField(max_length=50, null=False)
    circonstance = models.CharField(max_length=50, null=False)
    scenario = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    investigateur = models.ForeignKey(to=Investigateur, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.nom} - {self.investigateur.joueur.username}"


class SavoirImpie(models.Model):
    """"""

    CHOICE_SAVOIR = {
        ("Créatures connues", "Créatures connues"),
        ("Ouvrages consultés", "Ouvrages consultés"),
    }
    type = models.CharField(max_length=20, choices=CHOICE_SAVOIR)
    nom = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    investigateur = models.ForeignKey(to=Investigateur, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Savoir Impie"
        verbose_name_plural = "Savoirs Impies"

    def __str__(self):
        return f"{self.nom} - {self.investigateur.joueur.username}"
