from Receitas import views
from django.test import TestCase
from django.urls import reverse, resolve

class ReceitasViewsTest(TestCase):

    def test_recipes_index_view_function_is_correct(self):
        view = resolve(reverse('recipes:index'))
        self.assertIs(view.func, views.index)
    
    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)
    
    '''
    def test_recipes_index_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_index_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertTemplateUsed(response, 'receitas/pages/index.html')
    '''
