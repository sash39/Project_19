from django.shortcuts import render
from django.views.generic import FormView

from users.forms import UserRegistrationForm


class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    
