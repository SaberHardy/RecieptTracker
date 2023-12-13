from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['store_name', 'date_of_purchase', 'item', 'quantity', 'price', 'status']
