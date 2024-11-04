from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from apps.user.manager import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=10, null=True, blank=True, unique=False)
    phone_number = models.CharField(
        unique=True,
        null=True,
        max_length=13,
        validators=[RegexValidator(regex=r'^\+996\d{9}$',
                                   message="Format: '+996XXXXXXXXX'. Up to 12 digits allowed.")]
    )
    email = models.EmailField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.phone_number

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
