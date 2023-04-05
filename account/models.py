from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ """

    profile_picture = models.ImageField(upload_to="userpicture/", blank=True, null=True)
    profile_creation = models.DateTimeField(auto_now_add=True)
    profile_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Compte Utilisateur"
        verbose_name_plural = "Comptes Utilisateurs"

    def __str__(self):
        return f"{self.username} - {self.first_name} - {self.last_name}"
