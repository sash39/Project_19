from django.contrib.auth.models import BaseUserManager
from typing import Optional
from django.db.models import Model

class UserManager(BaseUserManager):
    def create_user(self, username: str, email: Optional[str] = ..., password: Optional[str] = ...,):
        pass

    def create_superuser(self, email: Optional[str], password: Optional[str]):
        user_model: type[Model] = self.model
        new_superuser = user_model(email=email, is_active=True, is_admin = True)
        new_superuser.set_password(password)
        new_superuser.save()

    def get_by_natural_key(self, username: Optional[str]):
        return self.model.objects.get(email=username)