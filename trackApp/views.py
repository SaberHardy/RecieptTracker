from django import http
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

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


# @login_required
# def create_receipt(request):
#     form = RecipeForm(request.POST or None)
#     if form.is_valid():
#         recipe = form.save()
#         # Optionally add success message to request context:
#         # request.session['success_message'] = "Recipe created successfully!"
#         return redirect('index')
#     else:
#         # Handle form errors gracefully (optional)
#         return render(request, 'trackApp/create_receipt.html', {'form': form})

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Recipe
from .forms import RecipeForm


class CreateReceiptView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'trackApp/create_receipt.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Associate the user with the receipt before saving
        form.instance.user = self.request.user  # Set the user to the currently logged-in user
        messages.success(self.request, 'Receipt created successfully.')
        return super().form_valid(form)


# @login_required
# def update_receipt(request, id):
#     context = {}
#
#     item_to_update = Recipe.objects.get(id=id)
#     form = RecipeForm(request.POST or None, instance=item_to_update)
#
#     if form.is_valid():
#         form.save()
#         return redirect("index")
#     else:
#         print("Form is not valid:", form.errors)
#
#     context['form'] = form
#     context['item_to_update'] = item_to_update
#     return render(request, "trackApp/update_item.html", context)

class UpdateReceiptView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'trackApp/update_item.html'

    def get_object(self, queryset=None):
        # Get the receipt object
        obj = super().get_object(queryset=queryset)

        # Check if the logged-in user is the owner of the receipt
        if self.request.user != obj.user:
            # You may want to raise a PermissionDenied or redirect to a permission denied page
            raise PermissionDenied("You do not have permission to update this receipt.")

        return obj

    def form_valid(self, form):
        # Ensure the logged-in user is the owner of the receipt being updated
        if self.request.user != self.get_object().user:
            # You may want to raise a PermissionDenied or redirect to a permission denied page
            raise PermissionDenied("You do not have permission to update this receipt.")

        return super().form_valid(form)
    # success_url = reverse_lazy('index')
