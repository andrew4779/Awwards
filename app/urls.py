
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("accounts/profile/", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),
    path("project/<int:project_id>/", views.project_details, name="project_details"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)