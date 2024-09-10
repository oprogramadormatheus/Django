from . import forms
from django.http import Http404
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
        return redirect(reverse('authors:login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                replace_list = ["{", "}", "'"]
                for i in replace_list:
                    error = error.replace(i, '')
                messages.error(request, error)
        
    return redirect('authors:register')

def login_view(request):

    form = forms.LoginForm()
    context = {
        'form': form,
        'form_action': reverse('authors:login_create')
    }
    return render(request, 'authors/pages/login.html', context)

def login_create(request):

    if not request.POST:
        raise Http404()
    
    form = forms.LoginForm(request.POST)
    login_url = reverse('authors:login')
    
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado')
            login(request, authenticated_user)
            return redirect(login_url)
        
        messages.error(request, 'Credenciais inválidas')
        return redirect(login_url)
    
    messages.error(request, 'Formulário incorreto')
    return redirect(login_url)

@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authors:login'))

    logout(request)
    return redirect(reverse('authors:login'))
