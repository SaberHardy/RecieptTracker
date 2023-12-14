from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(user_name=user_name, password=password)

        if user is not None:
            login(request, user)
            print("Logged in successfully")
            messages.error(request, 'You are now logged in as %s' % user_name)
            return redirect('index')
        else:
            print("Invalid username or password")
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        print("Invalid username or password second")
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
