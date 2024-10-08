import os
from . import models
from django.db.models import Q
from django.http import Http404
from django.contrib import messages
from sources.pagination import create_pagination
from django.shortcuts import render, get_list_or_404, get_object_or_404

PER_PAGE = int(os.environ.get('PER_PAGE', 6))

def index(request):

    recipes = get_list_or_404(models.Recipe.objects.filter(is_published=True).order_by('-id'))
    page_obj, pagination_range = create_pagination(request, recipes, PER_PAGE)

    context  = {
        'recipes': page_obj,
        'pagination_range': pagination_range
    }

    return render(request, 'recipes/pages/index.html', context)

def recipes(request, id):

    recipe = get_object_or_404(models.Recipe, pk=id, is_published=True)
    context = {'recipe': recipe, 'is_detail_page': True}
    return render(request, 'recipes/pages/recipes.html', context)

def category(request, category_id):
    
    recipes = get_list_or_404(models.Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))
    page_obj, pagination_range = create_pagination(request, recipes, PER_PAGE)
    category = recipes[0].category.name
    context  = {'recipes': page_obj, 'pagination_range': pagination_range, 'category': category}
    return render(request, 'recipes/pages/category.html', context)

def search(request):

    search_term = request.GET.get('search', '').strip()
    if not search_term:
        raise Http404()
    
    recipes = models.Recipe.objects.filter(
        Q(Q(title__icontains=search_term) | Q(description__icontains=search_term)),
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = create_pagination(request, recipes, PER_PAGE)
    
    context = {
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'search_term': search_term,
        'additional_url_query': f'&search={search_term}',
    }

    return render(request, 'recipes/pages/search.html', context)
