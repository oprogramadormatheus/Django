from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):

    email = forms.CharField(required=False, label='Email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'password': 'Senha',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ex: Matheus'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ex: Oliveira'}),
            'username': forms.TextInput(attrs={'placeholder': 'Ex: matheus.oliveira'}),
        }
    
    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        username_existis = User.objects.filter(username=username).exists()

        if username_existis:
            raise ValidationError({
                'Nome de usuário indisponível',
            })
        
        if len(password) < 10:
            raise ValidationError({
                'A senha deve ter no mínimo 10 caracteres',
            })
