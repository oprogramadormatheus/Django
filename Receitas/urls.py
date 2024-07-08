from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name="index"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),
    path('recipes/<int:id>/', views.recipes, name="recipe"),
    path('recipes/search/', lambda request: ..., name='search')
]
