from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png')
    bio = models.TextField()
    location = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.user.username + "'s profile"
        #return "user number " 
