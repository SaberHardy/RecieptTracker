from django import http
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from trackApp.forms import RecipeForm
from trackApp.models import Recipe


# TODO: add logger and alerts,
# TODO: ListView, DetailView, DeleteView, UpdateView
# TODO: FormView

# Create your views here.
# def index(request):
#     all_recipes = Recipe.objects.all()
#     context = {
#         'all_recipes': all_recipes
#     }
#     return render(request, 'trackApp/index.html', context)

class ListItems(ListView):
    model = Recipe
    template_name = 'trackApp/index.html'
    ordering = '-date_of_purchase'

    def get_context_data(self, *args, object_list=None, **kwargs):
        all_recipes = Recipe.objects.all()
        context = super(ListItems, self).get_context_data(*args, **kwargs)
        context['all_recipes'] = all_recipes
        return context


def login(request):
    return render(request, 'trackApp/login.html')


def register(request):
    return render(request, 'trackApp/register.html')


# @login_required
# def details(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     context = {
#         'recipe': recipe,
#     }
#     return render(request, 'trackApp/details.html', context)

class ReceiptDetail(DetailView):
    model = Recipe
    template_name = 'trackApp/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # recipe = get_object_or_404(Recipe, pk=self)
        return context


@login_required
def track_item(request):
    search_item = request.GET.get('search')
    items_found = None

    if search_item != "":
        items_found = Recipe.objects.filter(Q(id__icontains=search_item))
        if items_found.exists():
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


# @login_required
# def delete_item(request, id):
#     try:
#         item_to_delete = Recipe.objects.get(id=id)
#         item_to_delete.delete()
#         return HttpResponseRedirect(reverse('index'))
#     except Exception as e:
#         print("The item doesn't exists")
#         return HttpResponseRedirect(reverse('index'))

class DeleteReceiptView(DeleteView):
    model = Recipe
    template_name = 'trackApp/delete_receipt.html'
    success_url = reverse_lazy('index')


@login_required
def create_receipt(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        recipe = form.save()
        # Optionally add success message to request context:
        # request.session['success_message'] = "Recipe created successfully!"
        return redirect('index')
    else:
        # Handle form errors gracefully (optional)
        return render(request, 'trackApp/create_receipt.html', {'form': form})


@login_required
def update_receipt(request, id):
    context = {}

    item_to_update = Recipe.objects.get(id=id)
    form = RecipeForm(request.POST or None, instance=item_to_update)

    if form.is_valid():
        form.save()
        return redirect("index")
    else:
        print("Form is not valid:", form.errors)

    context['form'] = form
    context['item_to_update'] = item_to_update
    return render(request, "trackApp/update_item.html", context)
