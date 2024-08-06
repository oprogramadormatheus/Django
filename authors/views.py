from . import forms
from django.shortcuts import render

def register_view(request):
    form = forms.RegisterForm()
    
    context = {
        'form': form
    }

    return render(request, 'authors/pages/register.html', context)
