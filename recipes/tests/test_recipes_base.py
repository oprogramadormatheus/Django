from django.test import TestCase
from recipes.models import Category, Recipe
from django.contrib.auth.models import User

class RecipeMixin:

    def create_category(self, name='Category'):
        return Category.objects.create(name=name)
    
    def create_author(self, username='matheus.ricardo', first_name='Matheus', last_name='Ricardo', password='12345678'):
        return User.objects.create_user(username=username, first_name = first_name, last_name = last_name,  password=password)

    def create_recipe(self, is_published=True, category_data=None, author_data=None, slug='slug-test'):

        if category_data is None:
            category_data = {}
        
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category = self.create_category(**category_data),
            author = self.create_author(**author_data),
            title = 'Test Title',
            description = 'Test Description',
            slug = slug,
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Pessoas',
            preparation_steps = 'Test Preparation Steps',
            preparation_steps_is_html = False,
            is_published = is_published,
        )
    
    def create_recipe_in_batch(self, qtd=10):
        recipes = []
        for i in range(qtd):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            recipe = self.create_recipe(**kwargs)
            recipes.append(recipe)
        return recipes

class RecipesTestBase(TestCase, RecipeMixin):

    def setUp(self) -> None:
        return super().setUp()
