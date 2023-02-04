from typing import Optional
from django.contrib.auth.models import UserManager


class UserManager(UserManager):
    def create_user(self, username: str, email: Optional[str] = ..., password: Optional[str] = ...,):
        pass
    
    def create_superuser(self, email: Optional[str], password: Optional[str]):
        raise Exception(email, password)

    def get_by_natural_key(self, username: Optional[str]):
        return self.model.objects.filter(email=username).first()
