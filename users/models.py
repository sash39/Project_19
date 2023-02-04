from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name='Признак активности пользователя',
        default=False,
    )
    is_admin = models.BooleanField(
        verbose_name='Пользователь администратор',
        default=False,
    )
    
    objects = UserManager()
