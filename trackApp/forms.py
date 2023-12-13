from django import forms

from .models import Recipe
from django.forms import DateInput


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['store_name', 'date_of_purchase', 'item', 'quantity', 'price', 'status']
        widgets = {
            'date_of_purchase': DateInput(attrs={'type': 'date'}),
        }
