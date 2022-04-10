import imp
from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ExifTags
from .utils import rotate_image
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from socialmedia.settings import BASE_DIR
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png')
    bio = models.TextField()
    location = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.user.username + "'s profile"
        #return "user number " 

    def save(self):
        super().save()
        width = 300
        img = Image.open(self.image.path)

        if (img.width > width):
            if (img.width < img.height):
                img.thumbnail((int(img.width/img.height*width), width))
            else:
                img.thumbnail((width, int(img.width/img.height*width)))
            
            img.save(self.image.path)
@receiver(post_save, sender=Profile, dispatch_uid="update_image_profile")
def update_image(sender, instance, **kwargs):
    if instance.image:
        fullpath = os.path.join(BASE_DIR, instance.image.path)
        print(BASE_DIR)
        print(fullpath)
        rotate_image(fullpath)

