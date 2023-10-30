from django.db import models
from django.contrib.auth.models import User


class RecipeCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preparation_steps = models.TextField()
    preparation_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='recipe_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(RecipeCategory, through='RecipeCategoryRelation')

    def __str__(self):
        return self.name


class RecipeCategoryRelation(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)
