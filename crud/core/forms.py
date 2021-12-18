from django.forms import forms, ModelForm, PasswordInput
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
    username = CharField(help_text=None)
    email = EmailField(help_text=None)
    password1 = CharField(label="Password", widget=PasswordInput, help_text=None)
    password2 = CharField(label="Confirm Password", widget=PasswordInput, help_text=None)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
