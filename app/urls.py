from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('new-project/', views.postproject, name='newproject'),
    path('project/<id>', views.get_project, name='project'),
    path('search/', views.search_projects, name='search_projects'),
    path('api/projects', views.ProjectList.as_view()),
    path('api/profiles', views.ProfileList.as_view()),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)