from django import forms
from .models import Post
from .validators import video_file_extension


class PostCreationForm(forms.Form):
    message = forms.Textarea()
    img = forms.ImageField()
    video = forms.FileField()

    class Meta:
        model = Post
        fields = ['message', 'img', 'video']
