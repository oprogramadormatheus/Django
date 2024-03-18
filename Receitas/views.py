from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'receitas/index.html', context={'name': 'Matheus'})

def contact(request):
    return render(request, 'receitas/contato.html')

def about(request):
    return render(request, 'receitas/sobre.html')
