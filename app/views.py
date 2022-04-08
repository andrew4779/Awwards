from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .permissions import IsAdminOrReadOnly

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    projects = Projects.objects.all()
    context = {
    "projects":projects,
    }
    return render(request, 'index.html', locals())

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)

@login_required(login_url='/accounts/login/')
def updateprofile(request):
    projects = Projects.objects.all()
    posts = Profile.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    'posts':posts,
    'projects':projects,
    }

    return render(request, 'profile/edit_profile.html', context)



@login_required(login_url='/accounts/login/')
def profile(request):
    projects = Projects.objects.all()
    posts = Profile.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    'posts':posts,
    'projects':projects,
    }
    return render(request, 'profile/profile.html', context)



@login_required(login_url='/accounts/login/')
def postproject(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('/')
    else:
        form = ProjectForm()
    context = {
        'form':form,
    }
    return render(request, 'post_project.html', context)

@login_required(login_url='/accounts/login/')
def get_project(request, id):
    project = Projects.objects.get(pk=id)

    return render(request, 'project.html', {'project':project})

@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET["project"]
        searched_projects = Projects.search_projects(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "projects": searched_projects})
    else:
        message = "You haven't searched for any user"

        return render(request, 'search.html', {"message":message})


class ProjectList(APIView):
    def get(self, request, format=None):
        allprojects = Projects.objects.all()
        serializers = ProjectSerializer(allprojects, many=True)
        return Response(serializers.data)
        permission_classes = (IsAdminOrReadOnly,)


class ProfileList(APIView):
    def get(self, request, format=None):
        allprofiles = Profile.objects.all()
        serializers = ProfileSerializer(allprofiles, many=True)
        return Response(serializers.data)
        permission_classes = (IsAdminOrReadOnly,)
