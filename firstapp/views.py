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
    return render(request, 'edit_recipe.html')


def add_recipe(request):
    return render(request, 'add_recipe.html')


def full_recipe(request):
    return render(request, 'full_recipe.html')


def recipe_list(request):
    return render(request, 'recipe_list.html')


def contacts(request):
    return render(request, 'contacts.html')
