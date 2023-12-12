from django.shortcuts import render
from trackApp.models import Recipe


# Create your views here.
def index(request):
    all_recipes = Recipe.objects.all()
    context = {
        'all_recipes': all_recipes
    }
    return render(request, 'trackApp/index.html', context)


def login(request):
    return render(request, 'trackApp/login.html')


def register(request):
    return render(request, 'trackApp/register.html')
