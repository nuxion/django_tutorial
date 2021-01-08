from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("about/<str:name>", views.about, name="about_name"),
    path("api/cursos", views.cursos_all, name="curso_all"),
    path("nuevo_curso", views.nuevo_curso, name="nuevo_curso"),
    path("api/cursos/<str:name>", views.cursos_one, name="curso_one")
]