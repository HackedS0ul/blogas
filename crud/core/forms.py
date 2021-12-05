from django.forms import forms, ModelForm
from django.forms.fields import EmailField, CharField
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreatePostForm(ModelForm):
    title = CharField(label="Name", help_text="Please enter your name")
    class Meta:
        model = Post
        fields = [
            'title',
            'short_desc',
            'description',
            'author',
            'status',
        ]


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']