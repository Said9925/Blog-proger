from django import forms
from proger.models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'cat']

    
