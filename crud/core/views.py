from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Post, Profile
from .forms import CreatePostForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, ProfileForm
from django.core.paginator import Paginator


class PostList(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 4

    # Old methods
    # a= Post.objects.all()
    # context = { 'items': a }
    # extra_context = {'items': 'Post.objects.count()'}
    # Updated methods
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Post.objects.count()
        return context


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


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'


def user_register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        return redirect('login')
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Your account is inactive!')
        else:
            return HttpResponse('Username or Password is incorrect!')

    return render(request, 'login.html', {})


def log_out(request):
    logout(request)
    return redirect('login')


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile.html'
    success_url = '/'
