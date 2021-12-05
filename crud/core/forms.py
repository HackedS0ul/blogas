from django.forms import forms, ModelForm
from django.forms.fields import EmailField, CharField
from .models import Post


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

