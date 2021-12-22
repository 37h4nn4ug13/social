from django.shortcuts import render, redirect
from posts.forms import PostCreationForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # this needs to be used to send a message that the user was successfully registered
            # username = form.cleaned_data.get('username')

            return redirect("home")
    else:
        form = PostCreationForm()
    context = {
        'form': form
    }
    return render(request, 'base/home.html', context)