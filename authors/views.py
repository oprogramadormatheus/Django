from . import forms
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.shortcuts import render, redirect

def register_view(request):
    
    register_form_data = request.session.get('register_form_data', None)
    form = forms.RegisterForm(register_form_data)
    context = {
        'form': form,
        'form_action': reverse("authors:register_create"),
    }

    return render(request, 'authors/pages/register.html', context)

def register_create(request):

    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = forms.RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Your user is created, please log in.')
        del(request.session['register_form_data'])
    else:
        for field, errors in form.errors.items():
            for error in errors:
                replace_list = ["{", "}", "'"]
                for i in replace_list:
                    error = error.replace(i, '')
                messages.error(request, error)
        
    return redirect('authors:register')

def login_view(request):
    return render(request, 'authors/pages/login.html')

def login_create(request):
    return render(request, 'authors/pages/login.html')
