from django.test import TestCase
from account.models import CustomUser
from warhammer.models import Campagne, Player

# Create your tests here.


class CampagneModelTestCase(TestCase):
    """Test for campagne model"""

    def setUp(self):
        self.campagne = Campagne.objects.create(
            nom_de_campagne="Campagne 01",
            date_debut="2023-05-01",
            date_end="2023-06-01",
            campagne_etat="En cours",
            maitre_du_jeu=CustomUser.objects.create_user(
                "Jeannot Jojo", "jeannot_jojo@maildejojo.com", "motdepasse"
            ),
        )

    def test_campagne_model_creation(self):
        self.assertTrue(isinstance(self.campagne, Campagne))
        self.assertEqual(
            self.campagne.__str__(),
            f"{self.campagne.nom_de_campagne} - {self.campagne.maitre_du_jeu}",
        )

    def test_campagne_model_retrieval(self):
        campagne = Campagne.objects.get(nom_de_campagne="Campagne 01")
        self.assertEqual(campagne, self.campagne)

    def test_campagne_model_01_update(self):
        self.campagne.campagne_etat = "En pause"
        self.campagne.save()
        campagne = Campagne.objects.get(nom_de_campagne="Campagne 01")
        self.assertEqual(campagne.campagne_etat, "En pause")

    def test_campagne_model_02_update(self):
        self.campagne.campagne_etat = "Terminée"
        self.campagne.save()
        campagne = Campagne.objects.get(nom_de_campagne="Campagne 01")
        self.assertEqual(campagne.campagne_etat, "Terminée")

    def test_campagne_model_deletion(self):
        self.campagne.delete()
        with self.assertRaises(Campagne.DoesNotExist):
            Campagne.objects.get(nom_de_campagne="Campagne 01")


class PlayerModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="Jeannot Jojo", password="motdepasse"
        )
        self.maitre_du_jeu = CustomUser.objects.create_user(
            username="Jeannette Jojo", password="motdepassejeanette"
        )
        self.campagne = Campagne.objects.create(
            nom_de_campagne="Campagne 02",
            date_debut="2023-05-01",
            date_end="2023-06-01",
            campagne_etat="En cours",
            maitre_du_jeu=self.maitre_du_jeu,
        )

    def test_create_player(self):
        player = Player.objects.create(
            nom="TestNomPlayer",
            race="Nain",
            sexe="Mâle",
            vocation="Guerrier",
            alignement="Loyal",
            age=30,
            taille="1m50",
            poids=80,
            cheveux="Brun",
            yeux="Bleus",
            joueur=self.user,
            campagne=self.campagne,
        )

        self.assertEqual(player.nom, "TestNomPlayer")
        self.assertEqual(player.race, "Nain")
        self.assertEqual(player.sexe, "Mâle")
        self.assertEqual(player.vocation, "Guerrier")
        self.assertEqual(player.alignement, "Loyal")
        self.assertEqual(player.age, 30)
        self.assertEqual(player.taille, "1m50")
        self.assertEqual(player.poids, 80)
        self.assertEqual(player.cheveux, "Brun")
        self.assertEqual(player.yeux, "Bleus")
        self.assertEqual(player.joueur, self.user)
        self.assertEqual(player.campagne, self.campagne)

    def test_player_str_method(self):
        player = Player.objects.create(
            nom="TestNomPlayer",
            race="Nain",
            sexe="Mâle",
            vocation="Guerrier",
            alignement="Loyal",
            age=30,
            taille="1m50",
            poids=80,
            cheveux="Brun",
            yeux="Bleus",
            joueur=self.user,
        )

        self.assertEqual(str(player), "TestNomPlayer - Jeannot Jojo -  - ")
