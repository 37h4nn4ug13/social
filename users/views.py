import imp
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.urls import reverse

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


class PersonalProfile(FormMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse('profile')

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            request.user.email = form.cleaned_data.get('email')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_object(self, **kwargs):
        return self.request.user

    def get_context_data(self, *, object_list=None, args=None, **kwargs):


        context = super(PersonalProfile, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


def login_view(request):
    form = UserLoginForm()
    if (request.method == "POST"):
        form = UserLoginForm(request.POST)
    
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)
