from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import LoginView, SignUpView, MyProgressView,ForgotPasswordView

app_name = 'user'
urlpatterns = [
    url('login', LoginView.as_view(), name='login'),
    url('', SignUpView.as_view(), name='signup'),
    url('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    url('my-progress', login_required(MyProgressView.as_view(), login_url='/user/login'), name='myprogress')
]