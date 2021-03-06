from django.forms import forms, ModelForm, PasswordInput
from django.forms.fields import EmailField, CharField
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CreatePostForm(ModelForm):
    title = CharField(label="Name", help_text="Please enter your name")

    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        super(CreatePostForm, self).clean()
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            self.errors['title'] = self.error_class([
                'Minimum 5 chars required'
            ])
        if len(title) > 6:
            self.errors['title'] = self.error_class([
                'Max 6 chars '
            ])

        return self.cleaned_data


class RegisterForm(UserCreationForm):
    username = CharField(help_text=None)
    email = EmailField(help_text=None)
    password1 = CharField(label="Password", widget=PasswordInput, help_text=None)
    password2 = CharField(label="Confirm Password", widget=PasswordInput, help_text=None)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user_profile',
            'address',
            'education',
            'country',
            'state',
            'phone_number',
        ]
