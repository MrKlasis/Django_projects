from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE
from users.utils import create_token


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    token = models.CharField(max_length=100, default=create_token(), verbose_name='token')
    email_verify = models.BooleanField(default=False, verbose_name='верификация почты')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

