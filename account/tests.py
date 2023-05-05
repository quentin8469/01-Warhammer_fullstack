from django.test import TestCase
from account.models import CustomUser


class CustomUserTestCase(TestCase):
    """Test du model CustomUser"""

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            "Jeannot Jojo", "jeannot_jojo@maildejojo.com", "motdepasse"
        )

    def test_CustomUser_creation(self):
        self.assertTrue(isinstance(self.user, CustomUser))
        self.assertEqual(
            self.user.__str__(),
            f"{self.user.username} - {self.user.first_name} - {self.user.last_name}",
        )

    def test_CustomUser_retrieval(self):
        user = CustomUser.objects.get(username="Jeannot Jojo")
        self.assertEqual(user, self.user)

    def test_CustomUser_update(self):
        self.user.first_name = "Jeannot"
        self.user.save()
        user = CustomUser.objects.get(username="Jeannot Jojo")
        self.assertEqual(user.first_name, "Jeannot")

    def test_CustomUser_deletion(self):
        self.user.delete()
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(username="Jeannot Jojo")
