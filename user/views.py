from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from django.views import View
from django.urls import reverse

from .models import Profile


class LoginView(View):
    def get(self, request):
        return HttpResponse("Hello")

    def post(self, request):
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username, password)
        if user:
            login(request, user)
        else:
            return HttpResponse(status=404, data={'msg': 'Invalid User'})


class SignUpView(View):
    def get(self, request):
        return HttpResponse("Signup")

    def post(self, request):
        data = request.POST
        profile = Profile.objects.create_user(data['email'], data['password'], data['first_name'],
                                              data['last_name'], data['phone_number'])
        if profile:
            return HttpResponseRedirect(reverse('login'))
