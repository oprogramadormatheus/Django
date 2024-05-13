from . import models
from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe

def index(request):

    recipes = models.Recipe.objects.filter(is_published=True).order_by('-id')
    context  = {'recipes': recipes}
    return render(request, 'receitas/pages/index.html', context)

def recipes(request, id):

    recipe = models.Recipe.objects.filter(pk=id, is_published=True).first()
    context = {'recipe': recipe, 'is_detail_page': True}
    return render(request, 'receitas/pages/recipes.html', context)

def category(request, category_id):
    
    recipes = get_list_or_404(models.Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))
    category = recipes[0].category.name
    context  = {'recipes': recipes, 'category': category}
    return render(request, 'receitas/pages/category.html', context)
