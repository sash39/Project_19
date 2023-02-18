from django.views.generic import FormView, RedirectView
from django.contrib.auth import login, logout
from django.http.response import HttpResponse
from django.urls import reverse_lazy

from users.forms import UserRegistrationForm, UserLoginForm
from users.services import UserService


class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    # success_url = reverse('users:login') TODO: сделать страницу авторизации

    def form_valid(self, form: UserRegistrationForm) -> HttpResponse:
        user_service = UserService()
        user_service.create_user(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        return super().form_valid(form)


class UserLoginView(FormView):
    template_name = 'sign/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')
    
    def get(self, request, *args: str, **kwargs) -> HttpResponse:
        print(request.user)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: UserLoginForm) -> HttpResponse:
        user_service = UserService()
        user = user_service.get_user(email=form.cleaned_data['email'])
        login(self.request, user)
        return super().form_valid(form)


class UserLogoutView(RedirectView):
    url = reverse_lazy('index')
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
