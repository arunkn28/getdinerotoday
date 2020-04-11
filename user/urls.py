from .views import LoginView, SignUpView,ForgotPasswordView
from django.conf.urls import url

urlpatterns = [
    url('login', LoginView.as_view(), name='login'),
    url('signup', SignUpView.as_view(), name='signup'),
    url('forgot', ForgotPasswordView.as_view(), name='forgot')
]