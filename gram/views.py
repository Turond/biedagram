from django.shortcuts import render, redirect
from .forms import UserSignupForm, PostForm
from django.contrib.auth import authenticate

# Create your views here.

def homepage(request):
    return render(request, 'gram/home.html',{})

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=user_password,email=email)
            return redirect('/')
        else:
            return render(request, 'gram/signup.html', {'form': form})
    else:
        form = UserSignupForm()
        return render(request,'gram/signup.html', {'form': form})

def image_upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    else:
        form = PostForm
        return render(request,'gram/image_upload.html', {'form': form})