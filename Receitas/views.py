from django.shortcuts import render
from utils.recipes.factory import make_recipe
from . import models
from django.http import Http404

def index(request):

    recipes = models.Recipe.objects.filter(is_published=True).order_by('-id')

    context  = {'recipes': recipes}
    return render(request, 'receitas/pages/index.html', context)

def recipes(request, id):

    context = {'recipe': make_recipe(), 'is_detail_page': True}
    return render(request, 'receitas/pages/recipes.html', context)

def category(request, category_id):

    recipes = models.Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    try:
        category_name = models.Category.objects.filter(id=category_id)[0]
    except IndexError:
        raise Http404('Not Found')

    context  = {'recipes': recipes, 'category_name': category_name}
    return render(request, 'receitas/pages/category.html', context)
