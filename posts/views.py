from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Post, Comment


# Create your views here.
class PostListView(ListView):
    model = Post

def PostList(request):
    context = {
        "posts": Post.objects.all(),
        "comments": Comment.objects.all()
    }
    return render(request, 'posts/posts_list.html', context)


class PostCreateView(CreateView):
    model = Post
    fields = ['message', 'img', 'video']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# def like_req(request):
#     if request.method == "POST":
#