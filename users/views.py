
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .forms import ProfileUpdateForm, UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from posts.models import Post
from django.contrib.auth import logout, login, authenticate


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])

            login(request, new_user)
            messages.add_message(request, messages.SUCCESS, f"Account for { new_user.get_username } has been created🥳")
            # username = form.cleaned_data.get('username')

            # This is definitely not a url that should be used
            return redirect("profile")
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile_view(request):
    posts = Post.objects.all()
    
    user = request.user
    profile = request.user.profile
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'posts': posts,
        'user': user,
        'profile': profile
    }
    return render(request, 'users/profile.html', context)


def login_view(request):
    form = UserLoginForm()
    if (request.method == "POST"):
        form = UserLoginForm(request.POST)
    
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)
