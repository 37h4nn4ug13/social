from django.contrib import admin
from . import models as users_models

# Register your models here.
admin.site.register(users_models.Profile)