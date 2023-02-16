from django.forms import Form, EmailField, CharField, PasswordInput, EmailInput

from users.services import UserService


class UserRegistrationForm(Form):
    email = EmailField(label='Введите email', widget=EmailInput(
        attrs={
            'type': "email",
            'class': "form-control",
            'id': "exampleInputEmail",
            'aria-describedby': "emailHelp",
            'placeholder': "Enter email"
        }
    ))
    password = CharField(label='Введите пароль', widget=PasswordInput(attrs={'placeholder': "Введите пароль тут"}))
    confirm_password = CharField(label='Введите пароль', widget=PasswordInput(attrs={'placeholder': "Повторите пароль тут"}))

    def is_valid(self) -> bool:
        is_valid = super().is_valid()

        if not is_valid:
            return False

        user_service = UserService()
        errors = user_service.validate_registration(**self.cleaned_data)

        if len(list(errors.keys())) > 0:
            for field, field_errors in errors.items():
                for error in field_errors:
                    self.add_error(field, error)
            return False
        return True
