from django.shortcuts import render
from .models import Recipe, RecipeCategory


def main(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def register(request):
    return render(request, 'register.html')


def edit_recipe(request):
    return render(request, 'editrecipe.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = RecipeCategory.objects.all()
    context = {
        'recipes': recipes,
        'categories': categories,
    }
    return render(request, 'recipe_list.html', context)


def contacts(request):
    return render(request, 'contacts.html')
