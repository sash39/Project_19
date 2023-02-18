from collections import defaultdict
import string
from typing import Optional

from django.contrib.auth.hashers import make_password
from users.constants import USER_MIN_PASSWORD_LENGTH
from users.constants import USER_DIGIT_AND_SYMBOLS

from users.models import User


class UserService:
    model = User

    def check_passwords(self, password: str, confirm_password: str) -> Optional[list[str]]:
        errors = []

        if password != confirm_password:
            errors.append('Пароли не совпадают')
        if len(password) < USER_MIN_PASSWORD_LENGTH:
            errors.append(f'Длина пароля должна быть больше {USER_MIN_PASSWORD_LENGTH} символов')
        if not set(string.ascii_uppercase) & set(password):
            errors.append('Пароль должен содержать хотя бы одну заглавную букву.')
        if not set(password) & USER_DIGIT_AND_SYMBOLS:
            errors.append(f'Пароль должен содержать хотя бы один из специальных {USER_MIN_PASSWORD_LENGTH} символов')
        return errors

    def _user_exists(self, **kwargs) -> bool:
        return self.model.objects.filter(**kwargs).exists()

    def check_registration_email(self, email: str) -> Optional[list[str]]:
        errors = []

        if self._user_exists(email=email):
            errors.append('Пользователь с таким email уже зарегестрирован')
        return errors

    def validate_registration(
        self,
        email: str,
        password: str,
        confirm_password: str
    ) -> dict[str, list[str]]:
        errors = defaultdict(list)

        email_errors = self.check_registration_email(email)
        password_errors = self.check_passwords(password, confirm_password)

        if len(email_errors):
            errors['email'].extend(email_errors)
        if len(password_errors):
            errors['password'].extend(password_errors)
            errors['confirm_password'].extend(password_errors)
        return errors

    @staticmethod
    def _get_hashed_password(password: str) -> str:
        return make_password(password)

    @staticmethod
    def _save_user_to_db(user: User):
        user.save()

    def create_user(self, email: str, password: str) -> None:
        user = self.model(email=email)
        user.password = self._get_hashed_password(password)
        self._save_user_to_db(user)

    def get_user(self, **filters) -> Optional[User]:
        return self.model.objects.filter(**filters).first()

    def check_login_email(self, email: str) -> list[str]:
        user = self.get_user(email=email)

        if not user:
            return ['Данного пользователя не существует.']
        elif not user.is_active:
            return ['Данный пользователь не активен.']
        return []
    
    def check_password_correct(self, password: str, **filters) -> list[str]:
        user = self.get_user(**filters)
        
        if not user.check_password(password):
            return ['Неверный пароль.']
        return []

    def validate_login(self, email: str, password: str) -> dict[str, list]:
        errors = defaultdict(list)
        
        email_errors = self.check_login_email(email)

        if len(email_errors):
            errors['email'].extend(email_errors)
            return errors

        password_errors = self.check_password_correct(password, email=email)

        if len(password_errors):
            errors['password'].extend(password_errors)
        return errors
