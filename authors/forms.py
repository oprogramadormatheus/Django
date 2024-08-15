from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita sua senha',
        }),
        help_text='A senha deve ser igual a que você digitou anteriormente',
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password': 'Senha',
            'password2': 'Confirmar Senha'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Crie um usuário',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Crie uma senha',
            })
        }

    def clean(self):

        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Password and Password2 must be equal',
                'password2': 'Password and Password2 must be equal',
            })
