from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("about/<str:name>", views.about, name="about_name")
]