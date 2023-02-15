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



# from django.shortcuts import  render, redirect
# from .forms import UserRegistrationView
# from django.contrib.auth import login
# from django.contrib import messages
#
# def register_request(request):
# 	if request.method == "POST":
# 		form = UserRegistrationView(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("main:homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = UserRegistrationForm()
# 	return render (request=request, template_name='registration.html', context={"register_form":form})

    # def register(self, request):
    #     if request.method == 'POST':
    #         form = UserRegistrationForm(request.POST)
    #         if form.is_valid():
    #             new_user = form.save(commit=False)
    #             new_user.set_password(form.cleaned_data['password1'])
    #             new_user.save()
    #
    #             return render(request, 'blog/post/list.html', {'new_user': new_user})
    #     else:
    #         return render(request, 'oauth/user/registration_form.html', {'form': form})