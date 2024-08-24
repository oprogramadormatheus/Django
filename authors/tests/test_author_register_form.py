from unittest import TestCase
from django.urls import reverse
from authors.forms import RegisterForm
from parameterized import parameterized
from django.test import TestCase as DjangoTestCase

class AuthorRegisterFormUnitTest(TestCase):

    @parameterized.expand([
        ('first_name', 'Ex: Matheus'),
        ('last_name', 'Ex: Oliveira'),
        ('username', 'Ex: matheus.oliveira'),
    ])
    def test_fields_placeholder(self, field, needed):
        form = RegisterForm()
        current = form[field].field.widget.attrs['placeholder']
        self.assertEqual(needed, current)

    @parameterized.expand([
        ('first_name', 'Nome'),
        ('last_name', 'Sobrenome'),
        ('username', 'Usuário'),
        ('email', 'Email'),
        ('password', 'Senha'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(needed, current)

class AuthorRegisterFormIntegrarionTest(DjangoTestCase):

    def setUp(self) -> None:
        self.form_data = {
            'first_name': 'first',
            'last_name': 'last',
            'username': 'first.last',
            'email': 'email@email.com',
            'password': 'djangopassword',
        }
        return super().setUp()
    
    def test_password_min_length_is_10(self):

        self.form_data['password'] = '123'
        msg = 'A senha deve ter no mínimo 10 caracteres'
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_username_field_must_be_unique(self):

        url = reverse('authors:register_create')
        msg = 'Nome de usuário indisponível'
        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
    
    def test_authors_create_returns_404_if_request_method_is_get(self):

        url = reverse('authors:register_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_author_can_login(self):
        url = reverse('authors:register_create')
        self.client.post(url, data=self.form_data, follow=True)
        is_authenticated = self.client.login(username='first.last', password='djangopassword')
        self.assertTrue(is_authenticated)
