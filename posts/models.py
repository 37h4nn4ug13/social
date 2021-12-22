from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .validators import video_file_extension


# Create your models here.
class Post(models.Model):
    message = models.CharField(max_length=400)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/postImg', blank=True)
    video = models.FileField(upload_to='media/postVideo', blank=True, validators=[video_file_extension])

    def __str__(self):
        return f"{ self.author.username } { self.date }"

    def get_absolute_url(self):
        return reverse('posts-list')

    class Meta:
        ordering = ['-id']
