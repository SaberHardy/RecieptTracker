from django.db.models import Q
from django.shortcuts import render, get_object_or_404

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


def details(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe': recipe,
    }
    return render(request, 'trackApp/details.html', context)


def track_item(request):
    search_item = request.GET.get('search')
    items_found = None

    if search_item != "":
        items_found = Recipe.objects.filter(Q(id__icontains=search_item))
        if items_found.exists():
            # TODO: add logger and alerts
            print("Item exists in the database!")
        else:
            print("Item doesn't exist in the database.")
    else:
        print("No search item provided")

    # recipe = get_object_or_404(Recipe, id=id)
    context = {
        "items_found": items_found,
    }

    return render(request, 'trackApp/track_item.html', context)
