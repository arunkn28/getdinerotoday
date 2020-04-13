from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.views import View
from django.urls import reverse

from .models import Profile
from django.shortcuts import render


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, 'login.html', {'error': "Either username or password is incorrect"})


class SignUpView(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        data = request.POST
        try:
            profile = Profile.objects.create_user(data['email'], data['password'], data['first_name'],
                                                  data['last_name'], data['phone_number'])
        except Exception as e:
            return render(request, 'registeration.html', {"error": "Registeration Failed"})
        if profile:
            return HttpResponseRedirect(reverse('user:login'))


class PasswordResetView(auth_views.PasswordResetView):
    @property
    def template_name(self):
        return 'forgotpassword.html'

    @property
    def success_url(self):
        return reverse('user:password_reset_done')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    @property
    def template_name(self):
        return 'resetPassword.html'

    @property
    def success_url(self):
        return reverse('user:password_change_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    @property
    def template_name(self):
        return 'password-reset-email-sent.html'


class PasswordChangeDoneView(View):
    def get(self, request):
        return render(request, 'login.html', {"password_change_msg": "Successfully changed password"})


class MyProgressView(View):
    def get(self, request):
        return render(request, "home/my_progress.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('user:login'))
