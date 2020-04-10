from .views import LoginView, SignUpView
from django.conf.urls import url

urlpatterns = [
    url('login', LoginView.as_view(), name='login'),
    url('signup', SignUpView.as_view(), name='signup')
]