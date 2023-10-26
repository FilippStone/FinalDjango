from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.logout, name='register'),
    #path('add/', views.add_recipe, name='add_recipe')
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('contacts/', views.contacts, name='contacts')
]
