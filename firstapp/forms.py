from django import forms
from .models import Recipe, RecipeCategory


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description',
                  'ingredients', 'instructions', 'preparation_time', 'image', 'author', ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = RecipeCategory
        fields = ['name']
