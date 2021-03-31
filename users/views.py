from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account, {username} Created Successfully!')
            return redirect('register-user')
    else:

        form = UserCreationForm
    return render(request, 'users/user-register.html', {'form': form})


def home(request):
    return render(request, 'users/user-home.html')