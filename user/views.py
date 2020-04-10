from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse

from .models import Profile


class LoginView(View):
    def get(self, request):
        return HttpResponse("Hello")


class SignUpView(View):
    def get(self, request):
        return HttpResponse("Signup")

    def post(self, request):
        data = request.POST
        profile = Profile.objects.create_user(data['email'], data['password'], data['first_name'],
                                    data['last_name'], data['phone_number'])
        if profile:
            return HttpResponseRedirect(reverse('login'))
