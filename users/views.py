from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView, ListView

from .forms import UserRegisterForm, UserLoginForm
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
            # this needs to be used to send a message that the user was successfully registered
            # username = form.cleaned_data.get('username')

            # This is definitely not a url that should be used
            return redirect("profile")
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


class PersonalProfile(DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_object(self, **kwargs):
        return self.request.user

    def get_context_data(self, *, object_list=None, args=None, **kwargs):
        context = super(PersonalProfile, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


def login_view(request):
    context = {
        'form': UserLoginForm
    }
    return render(request, 'users/login.html', context)
