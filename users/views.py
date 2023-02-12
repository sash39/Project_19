from django.views.generic import FormView
from django.http.response import HttpResponse

from users.forms import UserRegistrationForm
from users.services import UserService


class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = '/login'
    # success_url = reverse('users:login') TODO: сделать страницу регистрации

    def form_valid(self, form: UserRegistrationForm) -> HttpResponse:
        user_service = UserService()
        user_service.create_user(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        return super().form_valid(form)
        
