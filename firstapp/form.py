# from django.shortcuts import render, redirect
# from .forms import RecipeForm
# from .models import Recipe
#
#
# def add_recipe(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('recipe_list')
#     else:
#         form = RecipeForm()
#
#     return render(request, 'add_recipe.html', {'form': form})
#
#
# def edit_recipe(request, recipe_id):
#     recipe = Recipe.objects.get(id=recipe_id)
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('recipe_list')
#     else:
#         form = RecipeForm(instance=recipe)
#
#     return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})
#
#
# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'recipe_list.html', {'recipes': recipes})