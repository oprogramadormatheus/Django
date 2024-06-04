from Receitas import views
from django.test import TestCase
from django.urls import reverse, resolve
from Receitas.models import Category, Recipe
from django.contrib.auth.models import User

class ReceitasViewsTest(TestCase):

    def test_recipes_index_view_function_is_correct(self):
        view = resolve(reverse('recipes:index'))
        self.assertIs(view.func, views.index)
    
    def test_recipes_index_loads_recipes(self):

        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            username='username',
            first_name = 'user',
            last_name = 'name', 
            password='123456',
        )
        recipes = Recipe.objects.create(
            category = category,
            author = author,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porçoes',
            preparation_steps = 'Recipe Preparation Steps',
            preparation_steps_is_html = False,
            is_published = True,
        )
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['recipe'].title, 'Recipe Title')
    
    '''
    def test_recipes_index_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_index_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertTemplateUsed(response, 'receitas/pages/index.html')
    '''
    
    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)
