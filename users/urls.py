from django.urls import path
from . import views as user_views

urlpatterns = [
    path('', user_views.PersonalProfile.as_view(), name='profile'),
    ]
