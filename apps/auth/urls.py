from apps.auth.views.login import LoginView
from apps.auth.views.logout import LogoutView
from apps.auth.views.me import MeView
from apps.auth.views.register import RegisterView
from django.urls import path

urlpatterns = [
    path("auth/login/email/", LoginView.as_view(), name="login-email"),
    path("auth/register/email/", RegisterView.as_view(), name="register"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/me/", MeView.as_view(), name="me-user"),
]
