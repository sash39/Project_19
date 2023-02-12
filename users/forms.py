from django.forms import Form, EmailField, CharField, PasswordInput


class UserRegistrationForm(Form):
    email = EmailField(label='Введите email')
    password = CharField(label='Введите пароль', widget=PasswordInput())
