from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):

    email = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password': 'Senha',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Crie um usuário',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Crie uma senha',
            }),
        }

    def clean(self):

        password = self.cleaned_data.get('password')
        if len(password) < 10:
            raise ValidationError({
                'A senha deve ter no mínimo 10 caracteres',
            })
