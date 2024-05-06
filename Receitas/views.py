from django.shortcuts import render
from utils.recipes.factory import make_recipe

def index(request):
    context  = {'recipes': [make_recipe() for _ in range(10)]}
    return render(request, 'receitas/pages/index.html', context)

def recipes(request, id):

    context = {'recipe': make_recipe(), 'is_detail_page': True}
    return render(request, 'receitas/pages/recipes.html', context)
