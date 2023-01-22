from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from proger.models import Category, Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'cat']

    
