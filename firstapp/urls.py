from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.add_recipe, name='add'),
    path('edit/', views.edit_recipe, name='edit'),
    path('full/', views.full_recipe, name='full'),
    path('recipes/', views.recipe_list, name='recipes'),
    path('contacts/', views.contacts, name='contacts')
]
