from django.shortcuts import render

def index(request):
    return render(request, 'receitas/pages/index.html')

def recipes(request, id):
    return render(request, 'receitas/pages/recipes.html')
