from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import LoginView, SignUpView, MyProgressView, ForgotPasswordView, LogoutView,\
                ResetPasswordView

app_name = 'user'
urlpatterns = [
    url('login', LoginView.as_view(), name='login'),
    url('logout', LogoutView.as_view(), name='logout'),
    url('signup', SignUpView.as_view(), name='signup'),
    url('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    url('reset-password', ResetPasswordView.as_view(), name='reset-password'),
    url('my-progress', login_required(MyProgressView.as_view(), login_url='/user/login'), name='myprogress')
]