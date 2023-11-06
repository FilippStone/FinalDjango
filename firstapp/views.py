from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm, CategoryForm
from .models import Recipe
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def main(request):
    recipes = Recipe.objects.order_by('?')[:5]
    print(recipes)

    context = {
        'recipes': recipes,
    }

    return render(request, 'index.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        else:
            for field, errors in form.errors.items():
                print(f"Validation errors for field {field}: {errors}")
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def edit_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('main', recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'edit_recipe.html', {'form': form})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()
            return redirect('main')
    else:
        form = RecipeForm()

    return render(request, 'add_recipe.html', {'form': form})



@login_required()
def recipe_list(request, user=None):
    if user:
        user_obj = User.objects.filter(username=user).first()
        if user_obj:
            recipes = Recipe.objects.filter(author=user_obj)
        else:
            recipes = []
    else:
        recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_list.html', context)


def contacts(request):
    return render(request, 'contacts.html')
