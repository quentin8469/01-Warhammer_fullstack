from django.contrib import admin
from account.models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "profile_picture", "profile_update")
