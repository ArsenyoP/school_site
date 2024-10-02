from django.urls import path

from teachers.views import add_subject, teachers_catalog, add_teacher
from users.views import login

app_name = "teachers"


urlpatterns = [
    path("main/", teachers_catalog, name="index"),
    path("login/", login, name="login"),
    path("add_subject/", add_subject, name="add_subject"),
    path("add_teacher/", add_teacher, name="add_teacher")
]
