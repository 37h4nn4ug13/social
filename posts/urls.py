from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('', views.PostListView.as_view(template_name='posts/posts_list.html'), name='posts-list'),
    path('', views.PostList, name='posts-list'),
    path('new/', views.PostCreateView.as_view(), name="new-post"),
]
