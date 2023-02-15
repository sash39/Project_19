from collections import defaultdict
from typing import Optional

from django.contrib.auth.hashers import make_password

from users.models import User


class UserService:
    model = User

    def check_passwords(self, password: str, confirm_password: str) -> Optional[list[str]]:
        errors = []

        if password != confirm_password:
            errors.append('Пароли не совпадают')
        if len(password) < 6: # TODO: вынести в константы минимальную длину пароля
            errors.append('Длина пароля должна быть больше 6 символов')
        return errors

    def _user_exists(self, **kwargs) -> bool:
        return self.model.objects.filter(**kwargs).exists()

    def check_email(self, email: str) -> Optional[list[str]]:
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

        email_errors = self.check_email(email)
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