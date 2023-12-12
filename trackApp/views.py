from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'trackApp/index.html')


def login(request):
    return render(request, 'trackApp/login.html')


def register(request):
    return render(request, 'trackApp/register.html')
