from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from account.models import CustomUser
from django.contrib.auth import authenticate, login
from django.template import Template, Context


class HomeViewTestCase(TestCase):
    """Test de la home view"""

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="Jeannot Jojo", password="motdepasse"
        )
        self.client = Client()
        self.url = reverse("home:acceuil")
        self.client.login(username="Jeannot Jojo", password="motdepasse")

    def test_homeview_with_authenticated_user(self):
        self.client.force_login(
            CustomUser.objects.create_user(username="testuser", password="testpass")
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homeTemplate/liste/liste_jdr.html")

    def test_homeview_status_code(self):
        response = self.client.get(reverse("home:acceuil"))
        self.assertEqual(response.status_code, 200)

    def test_homeview_template_used(self):
        response = self.client.get(reverse("home:acceuil"))
        self.assertTemplateUsed(response, "homeTemplate/liste/liste_jdr.html")

    def test_homeview_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("home:acceuil"))
        self.assertRedirects(response, "/account/connexion/?next=%2F")

    def test_homeview_context(self):
        response = self.client.get(reverse("home:acceuil"))
        self.assertIsInstance(response.context["user"], CustomUser)

    def test_homeview_html_content(self):
        response = self.client.get(reverse("home:acceuil"))
        self.assertContains(response, "<h1>Liste des jeux de rôle</h1>")
