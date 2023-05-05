from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    date_debut = models.DateField(null=True, blank=True)
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
    age = models.PositiveIntegerField(blank=True, null=True, default=0)
    taille = models.CharField(max_length=50, blank=True, null=True)
    poids = models.PositiveIntegerField(blank=True, null=True, default=0)
    cheveux = models.CharField(max_length=50, blank=True, null=True)
    yeux = models.CharField(max_length=50, blank=True, null=True)
    photo_personnage = models.ImageField(
        upload_to="photo_perso/", blank=True, null=True
    )
    point_destin = models.PositiveIntegerField(blank=True, null=True, default=0)
    debouches = models.TextField(blank=True, null=True, default="Ajouter débouchés")
    point_folie = models.PositiveIntegerField(blank=True, null=True, default=0)
    langue = models.CharField(max_length=50, blank=True, null=True, default="A définir")
    note = models.TextField(blank=True, null=True, default="Aucune note")
    mort_tuer = models.TextField(blank=True, null=True, default="Ajouter morts tués")

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


class PointDeDestin(models.Model):
    """"""

    pdd_actuel = models.IntegerField(blank=True, null=True, default=0)
    pdd_depense = models.PositiveIntegerField(blank=True, null=True, default=0)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Point de destin"
        verbose_name_plural = "Points de destins"

    def pdd_total(self):
        pdd_total = self.pdd_actuel + self.pdd_depense
        return pdd_total


class ExperiencePersonnage(models.Model):
    """ """

    xp_actuelle = models.PositiveIntegerField(blank=True, null=True, default=0)
    xp_depense = models.PositiveIntegerField(blank=True, null=True, default=0)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def xp_total(self):
        xp_total = self.xp_actuelle + self.xp_depense
        return xp_total


class DescriptionPersonnelle(models.Model):
    """ """

    lieu_naissance = models.CharField(
        max_length=150, blank=True, null=True, default="A définir"
    )
    signe_distinctif = models.TextField(blank=True, null=True, default="A définir")
    Membre_famille = models.TextField(blank=True, null=True, default="A définir")
    description_perso = models.TextField(blank=True, null=True, default="A définir")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Description Personnelle"
        verbose_name_plural = "Descriptions Personnelles"


class CaracteristiqueBase(models.Model):
    """"""

    mouvement = models.PositiveIntegerField(blank=False, null=False, default=0)
    capacite_combat = models.PositiveIntegerField(blank=False, null=False, default=0)
    capacité_tir = models.PositiveIntegerField(blank=False, null=False, default=0)
    force = models.PositiveIntegerField(blank=False, null=False, default=0)
    endurance = models.PositiveIntegerField(blank=False, null=False, default=0)
    point_blessure = models.PositiveIntegerField(blank=False, null=False, default=0)
    initiative = models.PositiveIntegerField(blank=False, null=False, default=0)
    nb_attaque = models.PositiveIntegerField(blank=False, null=False, default=0)
    dexterite = models.PositiveIntegerField(blank=False, null=False, default=0)
    commandement = models.PositiveIntegerField(blank=False, null=False, default=0)
    intelligence = models.PositiveIntegerField(blank=False, null=False, default=0)
    calme = models.PositiveIntegerField(blank=False, null=False, default=0)
    force_mentale = models.PositiveIntegerField(blank=False, null=False, default=0)
    sociabilite = models.PositiveIntegerField(blank=False, null=False, default=0)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Caracteristique de base"
        verbose_name_plural = "Caracteristiques de bases"


class PlanCarriere(models.Model):
    """"""

    nom = models.CharField(max_length=50, blank=True, null=True, default="A définir")
    mouvement = models.PositiveIntegerField(default=0)
    capacite_combat = models.PositiveIntegerField(default=0)
    capacité_tir = models.PositiveIntegerField(default=0)
    force = models.PositiveIntegerField(default=0)
    endurance = models.PositiveIntegerField(default=0)
    point_blessure = models.PositiveIntegerField(default=0)
    initiative = models.PositiveIntegerField(default=0)
    nb_attaque = models.PositiveIntegerField(default=0)
    dexterite = models.PositiveIntegerField(default=0)
    commandement = models.PositiveIntegerField(default=0)
    intelligence = models.PositiveIntegerField(default=0)
    calme = models.PositiveIntegerField(default=0)
    force_mentale = models.PositiveIntegerField(default=0)
    sociabilite = models.PositiveIntegerField(default=0)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Plan de carriere"
        verbose_name_plural = "Plans de carrieres"


class CaracteristiqueActuelle(models.Model):
    """"""

    mouvement = models.PositiveIntegerField(blank=True, null=True, default=0)
    capacite_combat = models.PositiveIntegerField(blank=True, null=True, default=0)
    capacité_tir = models.PositiveIntegerField(blank=True, null=True, default=0)
    force = models.PositiveIntegerField(blank=True, null=True, default=0)
    endurance = models.PositiveIntegerField(blank=True, null=True, default=0)
    point_blessure = models.PositiveIntegerField(blank=True, null=True, default=0)
    initiative = models.PositiveIntegerField(blank=True, null=True, default=0)
    nb_attaque = models.PositiveIntegerField(blank=True, null=True, default=0)
    dexterite = models.PositiveIntegerField(blank=True, null=True, default=0)
    commandement = models.PositiveIntegerField(blank=True, null=True, default=0)
    intelligence = models.PositiveIntegerField(blank=True, null=True, default=0)
    calme = models.PositiveIntegerField(blank=True, null=True, default=0)
    force_mentale = models.PositiveIntegerField(blank=True, null=True, default=0)
    sociabilite = models.PositiveIntegerField(blank=True, null=True, default=0)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Caracteristique actuelle"
        verbose_name_plural = "Caracteristiques actuelles"

    def encombrement_max(self):
        """
        Calcul l'encombrement maximal du personnage
        """
        return self.force * 100

    def init_att_list(self):
        """
        Calcul les initiatives en fonction du nombre d'attaque du personnage
        return un dictionnaire avec comme clé le nom et valeur une liste d'initiative
        """
        init_list = []
        inititive_calculer = {}
        if self.nb_attaque > 1:
            init_list.append(self.initiative)
            i = 1
            while i != self.nb_attaque:
                new_init = init_list[-1] / 2
                init_list.append(int(new_init))
                i += 1
            inititive_calculer[self.player.nom] = init_list
            return inititive_calculer
        init_list.append(self.initiative)
        inititive_calculer[self.player.nom] = init_list
        return inititive_calculer

    def init_list_tuple(self):
        """
        Calcul les initiatives en fonction du nombre d'attaque du personnage
        return une liste de tuple avec le nom et l'initiative [(nom,initiative)]
        """
        init_list = [(self.initiative, self.player.nom)]
        if self.nb_attaque > 1:
            delta_init = self.initiative / self.nb_attaque
            new_tuple_list = [(self.initiative, self.player.nom)]
            for i in range(1, self.nb_attaque):
                init_calk = int(new_tuple_list[-1][0] - delta_init)
                new_tuple_list.append((init_calk, self.player.nom))
            return new_tuple_list
        return init_list

    def deplacement_round(self):
        """
        Calcul le deplacement par round en fonction du mouvement du personnage
        return un dictionnaire
        """
        mouvement_round = {}
        mouvement_round["Prudent"] = self.mouvement * 2
        mouvement_round["Normale"] = self.mouvement * 4
        mouvement_round["Rapide"] = self.mouvement * 16
        return mouvement_round

    def deplacement_tour(self):
        """
        Calcul le deplacement par tour en fonction du mouvement du personnage
        return un dictionnaire
        """
        mouvement_tour = {}
        mouvement_tour["Prudent"] = self.mouvement * 12
        mouvement_tour["Normale"] = self.mouvement * 24
        mouvement_tour["Rapide"] = self.mouvement * 96
        return mouvement_tour

    def deplacement_kmh(self):
        """
        Calcul le deplacement en km/h en fonction du mouvement du personnage
        return un dictionnaire
        """
        mouvement_kmh = {}
        mouvement_kmh["Prudent"] = self.mouvement * 0.75
        mouvement_kmh["Normale"] = self.mouvement * 1.5
        mouvement_kmh["Rapide"] = self.mouvement * 5.75
        return mouvement_kmh


class PointDeBlessure(models.Model):
    """ """

    pdb_max = models.PositiveIntegerField(blank=True, null=True, default=0)
    pdb_actuel = models.IntegerField(blank=True, null=True, default=0)
    nb_blessure = models.PositiveIntegerField(blank=True, null=True, default=0)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Point de blessure"
        verbose_name_plural = "Points de blessures"

    @receiver(post_save, sender=CaracteristiqueActuelle)
    def update_pdb_max(sender, instance, **kwargs):
        """
        Utilisation du signal post_save pour mettre à jour pdb_max après
        la mise à jour des points de blessure du modèle CaracteristiqueActuelle.
        Il faut tout de même créer l'objet PointDeBlessure au préalable.
        """
        pdb_max = instance.point_blessure
        player = instance.player
        PointDeBlessure.objects.filter(player=player).update(pdb_max=pdb_max)


class Competence(models.Model):
    """ """

    nom = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    bonus = models.PositiveIntegerField(blank=True, null=True, default=0)
    malus = models.PositiveIntegerField(blank=True, null=True, default=0)
    apprentissage = models.TextField(blank=True, null=True)
    cout_xp = models.PositiveIntegerField(blank=True, null=True, default=0)
    niveau = models.CharField(max_length=50, blank=True, null=True, default="Initial")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Competence"
        verbose_name_plural = "Competences"

    def __str__(self):
        return f"{self.nom}"


class ArmeContact(models.Model):
    """"""

    nom = models.CharField(max_length=50, blank=False, null=False)
    initiative = models.IntegerField(blank=True, null=True, default=0)
    toucher = models.IntegerField(blank=True, null=True, default=0)
    degats = models.IntegerField(blank=True, null=True, default=0)
    parade = models.IntegerField(blank=True, null=True, default=0)
    encombrement = models.PositiveIntegerField(blank=True, null=True, default=0)
    note = models.TextField(blank=True, null=True, default="Aucune note")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Arme de contact"
        verbose_name_plural = "Armes de contacts"

    def __str__(self):
        return f"{self.nom}"


class ArmeDistance(models.Model):
    """"""

    nom = models.CharField(max_length=50, blank=False, null=False)
    porte_courte = models.PositiveIntegerField(blank=True, null=True, default=0)
    porte_longue = models.PositiveIntegerField(blank=True, null=True, default=0)
    porte_extreme = models.PositiveIntegerField(blank=True, null=True, default=0)
    force_effective = models.IntegerField(blank=True, null=True, default=0)
    armer_tirer = models.CharField(
        max_length=50, blank=True, null=True, default="A définir"
    )
    encombrement = models.PositiveIntegerField(blank=True, null=True, default=0)
    munitions = models.CharField(max_length=50, blank=True, null=True, default=0)
    nb_munitions = models.PositiveIntegerField(blank=True, null=True, default=0)
    note = models.TextField(blank=True, null=True, default="Aucune note")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Arme de distance"
        verbose_name_plural = "Armes de distances"

    def __str__(self):
        return f"{self.nom}"


class Armure(models.Model):
    """"""

    choix_loc = [
        ("Toutes", "Toutes"),
        ("Tête", "Tête"),
        ("Tronc", "Tronc"),
        ("Bras droit", "Bras droit"),
        ("Bras gauche", "Bras gauche"),
        ("Jambes droite", "Jambes droite"),
        ("Jambes gauche", "Jambes gauche"),
    ]

    nom = models.CharField(max_length=50, blank=False, null=False)
    protection = models.PositiveIntegerField(blank=True, null=True, default=0)
    localisation = models.CharField(max_length=50, choices=choix_loc)
    encombrement = models.PositiveIntegerField(blank=True, null=True, default=0)
    note = models.TextField(blank=True, null=True, default="Aucune note")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Armure"
        verbose_name_plural = "Armures"

    def __str__(self):
        return f"{self.nom} - {self.localisation}"


class Equipement(models.Model):
    """ """

    nom = models.CharField(max_length=50, blank=False, null=False)
    quantite = models.PositiveIntegerField(blank=True, null=True, default=0)
    encombrement = models.PositiveIntegerField(blank=True, null=True, default=0)
    note = models.TextField(blank=True, null=True, default="Aucune note")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Equipement"
        verbose_name_plural = "Equipements"

    def __str__(self):
        return f"{self.nom}"


class Bourse(models.Model):
    """"""

    couronne = models.PositiveIntegerField(blank=True, null=True, default=0)
    pistole = models.PositiveIntegerField(blank=True, null=True, default=0)
    sous = models.PositiveIntegerField(blank=True, null=True, default=0)
    encombrement = models.PositiveIntegerField(blank=True, null=True, default=0)
    autre = models.TextField(blank=True, null=True, default="A définir")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bourse"
        verbose_name_plural = "Bourses"

    def __str__(self):
        return f"{self.couronne} - {self.pistole} - {self.sous}"


class Magie(models.Model):
    """"""

    point_magie_personnage = models.IntegerField(blank=True, null=True, default=0)
    point_magie_actuel = models.IntegerField(blank=True, null=True, default=0)
    point_magie_supplementaire = models.IntegerField(blank=True, null=True, default=0)
    famillier_personnage = models.CharField(
        max_length=50, blank=True, null=True, default="Aucun famillier"
    )
    nombre_sort = models.PositiveIntegerField(blank=True, null=True, default=0)
    recuperation_pm = models.TextField(blank=True, null=True, default="A définir")
    armure_autorisee = models.TextField(blank=True, null=True, default="A définir")
    arme_non_autorisee = models.TextField(blank=True, null=True, default="A définir")
    niveau_magique = models.IntegerField(blank=True, null=True, default=0)
    niveau_pouvoir = models.IntegerField(blank=True, null=True, default=0)
    note = models.TextField(blank=True, null=True, default="Aucune note")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Magie"
        verbose_name_plural = "Magies"

    def __str__(self):
        return f"{self.player.nom}"

    def liste_points_magie(self):
        liste_pdm = []
        for i in range(self.point_magie_personnage):
            liste_pdm.append(i + 1)
        return liste_pdm


class Sortilege(models.Model):
    """"""

    choix_type_magie = [
        ("Magie mineure", "Magie mineure"),
        ("Magie de bataille", "Magie de bataille"),
        ("Magie démonique", "Magie démonique"),
        ("Magie druidique", "Magie druidique"),
        ("Magie élèmentaire", "Magie élèmentaire"),
        ("Magie illusoire", "Magie illusoire"),
        ("Magie nécromantique", "Magie nécromantique"),
        ("Magie autre", "Magie autre"),
    ]

    choix_niveau_sort = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    ]

    nom_sortilege = models.CharField(
        max_length=50, blank=False, null=False, default="A définir"
    )
    type_magie = models.CharField(max_length=50, choices=choix_type_magie)
    niveau_sort = models.CharField(max_length=50, choices=choix_niveau_sort)
    cout_point_magie = models.PositiveIntegerField(blank=True, null=True, default=0)
    porte = models.CharField(max_length=50, blank=True, null=True, default="A définir")
    duree = models.CharField(max_length=50, blank=True, null=True, default="A définir")
    degats = models.CharField(max_length=50, blank=True, null=True, default="A définir")
    composants = models.CharField(
        max_length=50, blank=True, null=True, default="A définir"
    )
    description_sort = models.TextField(
        blank=True, null=True, default="Ajouter description du sort"
    )
    incantation = models.TextField(
        blank=True, null=True, default="Incantation à définir"
    )
    apprentissage = models.CharField(
        max_length=50, blank=True, null=True, default="A définir"
    )
    cout_xp = models.PositiveIntegerField(blank=True, null=True, default=0)
    note = models.TextField(blank=True, null=True, default="Aucune note")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sortilege"
        verbose_name_plural = "Sortileges"

    def __str__(self):
        return f"{self.nom_sortilege} - {self.type_magie}"


class Monture(models.Model):
    """"""

    nom = models.CharField(max_length=50, blank=True, null=True, default="monture")
    mouvement = models.PositiveIntegerField(blank=True, null=True, default=0)
    capacite_combat = models.PositiveIntegerField(blank=True, null=True, default=0)
    capacité_tir = models.PositiveIntegerField(blank=True, null=True, default=0)
    force = models.PositiveIntegerField(blank=True, null=True, default=0)
    endurance = models.PositiveIntegerField(blank=True, null=True, default=0)
    point_blessure = models.PositiveIntegerField(blank=True, null=True, default=0)
    initiative = models.PositiveIntegerField(blank=True, null=True, default=0)
    nb_attaque = models.PositiveIntegerField(blank=True, null=True, default=0)
    dexterite = models.PositiveIntegerField(blank=True, null=True, default=0)
    commandement = models.PositiveIntegerField(blank=True, null=True, default=0)
    intelligence = models.PositiveIntegerField(blank=True, null=True, default=0)
    calme = models.PositiveIntegerField(blank=True, null=True, default=0)
    force_mentale = models.PositiveIntegerField(blank=True, null=True, default=0)
    sociabilite = models.PositiveIntegerField(blank=True, null=True, default=0)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Monture"
        verbose_name_plural = "Montures"


class EncombrementPersonnage(models.Model):
    pass
