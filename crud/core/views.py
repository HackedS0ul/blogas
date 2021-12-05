from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView,UpdateView
from .models import Post
from .forms import CreatePostForm


class PostList(ListView):
    model = Post
    template_name = 'index.html'


class PostCreate(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create.html'
    success_url = '/'


class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title',
        'short_desc',
        'description',
        'author',
        'status',
    ]
    template_name = 'update.html'
    success_url = '/'
