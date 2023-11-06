from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('edit_recipe/', views.edit_recipe, name='edit_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('contacts/', views.contacts, name='contacts'),
]
