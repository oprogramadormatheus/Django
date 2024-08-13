from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita sua senha',
            'class': 'password-input',
        }),
        help_text='A senha deve ser igual a que você digitou anteriormente'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'password2': 'Confirme sua senha'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Crie um usuário',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Crie uma senha',
            })
        }