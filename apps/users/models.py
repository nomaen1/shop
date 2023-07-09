from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserRegister(AbstractUser):
    bio = models.TextField(
        verbose_name="БИО",
        blank=True, null=True
    )
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"