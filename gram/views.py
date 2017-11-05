from django.shortcuts import render, redirect
from .forms import UserSignupForm
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
        form = UserSignupForm
        return render(request, 'gram/signup.html', {'form': form})