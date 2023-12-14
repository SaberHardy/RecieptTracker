from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()

    return render(request, 'registration/register.html')


def logout_user(request):
    logout(request)
    return redirect('index')
