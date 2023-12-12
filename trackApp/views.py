from django.shortcuts import render, get_object_or_404

from trackApp.models import Recipe, ItemModel


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


def details(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    all_items = ItemModel.objects.all()
    context = {
        'recipe': recipe,
        'all_items': all_items
    }
    return render(request, 'trackApp/details.html', context)
