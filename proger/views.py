from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from proger.models import Post
from proger.forms import AddPostForm
from proger.utils import DataMixin

class HomeView(DataMixin, ListView):
    model = Post
    template_name = 'proger/posts.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Post.objects.all()


class ShowPostView(DeleteView):
    model = Post
    template_name = 'proger/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class CategoryView(ListView):
    model = Post
    template_name = 'proger/posts.html'
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['post'][0].cat_id
        return context


class AbbPostView(LoginRequiredMixin ,CreateView):
    form_class = AddPostForm
    template_name = 'proger/add_post.html'
    success_url = reverse_lazy('home')
    raise_exception = True


