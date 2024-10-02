from django.urls import include

from django.contrib import admin
from django.urls import path
from main_page.views import index
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path("teachers/", include("teachers.urls", namespace="teachers")),
    path("users/", include("users.urls", namespace="users"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
