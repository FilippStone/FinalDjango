from django.contrib import admin
from .models import Recipe, RecipeCategory


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'preparation_time')


@admin.register(RecipeCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
