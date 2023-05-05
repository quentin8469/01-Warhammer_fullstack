from django.test import TestCase
from account.models import CustomUser
from warhammer.models import Campagne

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
