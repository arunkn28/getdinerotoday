from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

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
        else:
            return HttpResponseRedirect(reverse('login'))


class SignUpView(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        data = request.POST
        profile = Profile.objects.create_user(data['email'], data['password'], data['first_name'],
                                              data['last_name'], data['phone_number'])
        if profile:
            return HttpResponseRedirect(reverse('login'))


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'forgotPassword.html')



class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'resetPassword.html')




class MyProgressView(View):
    def get(self, request):
        return ""
