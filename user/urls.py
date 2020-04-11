from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import LoginView, SignUpView, MyProgressView,ForgotPasswordView

urlpatterns = [
    url('login', LoginView.as_view(), name='login'),
    url('signup', SignUpView.as_view(), name='signup'),
    url('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    url('my-progress', login_required(MyProgressView.as_view(), login_url='/user/login'), name='myprogress')
]