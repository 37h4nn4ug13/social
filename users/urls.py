from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.PersonalProfile.as_view(), name='profile'),
    ]
