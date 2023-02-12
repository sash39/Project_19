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
    
    @property
    def is_staff(self) -> bool:
        return self.is_admin

    @property
    def is_superuser(self) -> bool:
        return self.is_admin
    
    def has_module_permission(self, app_label: str) -> bool:
        return self.is_admin
    
    def has_module_perms(self, app_label: str) -> bool:
        return self.is_admin

    def has_perm(self, perm: str, obj: 'User' = None) -> bool:
        return self.is_admin

    objects = UserManager()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
