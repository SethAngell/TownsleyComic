from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=128, default="DoubleL Studio")
    bio = models.TextField(max_length=2048, null=True, blank=True)
    photo = models.ForeignKey(
        "content.ImageContent", on_delete=models.CASCADE, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name
