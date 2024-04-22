from django.shortcuts import render
from utils.recipes.factory import make_recipe

def index(request):

    context  = {'recipe_list': [make_recipe() for _ in range(10)]}
    return render(request, 'receitas/pages/index.html', context)

def recipes(request, id):

    context = {'recipe_list': make_recipe()}
    return render(request, 'receitas/pages/recipes.html', context)
