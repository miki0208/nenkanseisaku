from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
app_name = 'accounts'

urlpatterns = [
    path("",views.SignUpView.as_view(),name='signup'),
    path("signup_success/",views.SignUpSuccessView.as_view(),name="signup_success"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="logout.html"),name="logout"),
    path("profile/",views.ProfileView.as_view(template_name="profile.html"),name="profile"),
]