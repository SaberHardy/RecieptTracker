from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from members.forms import RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Logged in successfully")
            messages.success(request, 'You are now logged in as %s' % username)
            return redirect('index')
        else:
            print("Invalid username or password")
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    print("Redirected to login again!!")
    return render(request, 'registration/login.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"You are now logged in as {user.username}")
            print(f"User ID: {user.id}, Username: {user.username}")

            return redirect("index")
        # else:
        #     # Handle authentication failure
        # messages.error(request, 'Authentication failed. Please try logging in.')
    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')
