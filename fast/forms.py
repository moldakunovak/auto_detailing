from django import forms
from fast.models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("name", "description", "image")