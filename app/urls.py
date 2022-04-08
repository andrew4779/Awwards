
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
    path("project/save/", views.save_project, name="save_project"),
    path("project/<int:project_id>/", views.project_details, name="project_details"),
    path("project/delete/<int:id>/", views.delete_project, name="delete_project"),
    path("project/rate/<int:id>/", views.rate_project, name="rate_project"),
    path("search/", views.search_project, name="search_project"),
    # api
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)