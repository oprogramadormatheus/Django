from . import forms
from django.shortcuts import render

def register_view(request):

    if request.POST:
        form = forms.RegisterForm(request.POST)
    else:
        form = forms.RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'authors/pages/register.html', context)
