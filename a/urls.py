from django.urls import path
from . import views

app_name = "a"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.post, name="post"),
    path("page/<int:tweet_id>", views.page, name="page"),
    path("toukou/", views.toukou, name="toukou"),
]