from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['message', 'img', 'video']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
