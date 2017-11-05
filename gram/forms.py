from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post

class UserSignupForm(UserCreationForm):
    username = forms.CharField(help_text="pls logen xd")
    email = forms.EmailField(help_text="emel xd")

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

class UserSigninForm(AuthenticationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )

class PostForm(forms.ModelForm):

    class Meta:
        app_label = "gram"
        model = Post
        fields = (
            'title',
            'description',
            'image'
        )