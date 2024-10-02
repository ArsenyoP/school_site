from tkinter.font import names

from django.urls import path

from django.urls import include


from django.urls import path


from teachers.views import teachers_catalog

app_name = "main_page"

urlpatterns = [
    path("main/", teachers_catalog, name="index")
]

