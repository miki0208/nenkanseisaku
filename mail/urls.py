from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'mail'

urlpatterns = [
    path("send/", views.index, name="index"),
    path("", views.contact, name="contact"),
]
