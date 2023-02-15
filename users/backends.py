from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model



User: type(AbstractBaseUser) = get_user_model()

class SettingsBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.
    Use the login name and a hash of the password. For example:
    """

    def authenticate(self, request, username=None, password=None):
        authenticated_user = User.objects.filter(email=username).first()

        if not authenticated_user:
            return None
        elif authenticated_user.check_password(password):
            return authenticated_user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None