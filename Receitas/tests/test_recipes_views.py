from unittest import skip
from Receitas import views
from django.urls import reverse, resolve
from .test_recipes_base import ReceitasTestBase

class ReceitasViewsTest(ReceitasTestBase):

    @skip('WIP')
    def test_recipes_index_view_function_is_correct(self):
        view = resolve(reverse('recipes:index'))
        self.assertIs(view.func, views.index)
        
    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)
    

    def test_recipes_index_view_returns_200_if_recipes_found(self):
        self.create_recipe()
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_category_view_returns_200_if_recipes_found(self):
        self.create_recipe()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_recipe_view_returns_200_if_recipes_found(self):
        self.create_recipe()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
    

    def test_recipes_index_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 404)
    
    def test_recipes_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 404)
    
    def test_recipes_recipe_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
    
    
    def test_recipes_index_view_loads_correct_template(self):
        self.create_recipe()
        response = self.client.get(reverse('recipes:index'))
        self.assertTemplateUsed(response, 'receitas/pages/index.html')

    def test_recipes_category_view_loads_correct_template(self):
        self.create_recipe()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertTemplateUsed(response, 'receitas/pages/category.html')
    
    def test_recipes_recipe_view_loads_correct_template(self):
        self.create_recipe()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertTemplateUsed(response, 'receitas/pages/recipes.html')

    
    def test_recipes_index_loads_recipes(self):
        self.create_recipe(category_data={'name': 'Café da Manhã'})
        response = self.client.get(reverse('recipes:index'))
        content = response.content.decode('utf-8')
        self.assertIn('Matheus', content)
        self.assertIn('Café da Manhã', content)
    
    def test_recipes_category_loads_recipes(self):
        self.create_recipe(category_data={'name': 'Carnes Assadas'})
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn('Matheus', content)
        self.assertIn('Carnes Assadas', content)
    
    def test_recipes_recipe_loads_recipe(self):
        self.create_recipe(category_data={'name': 'Jantar'})
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn('Matheus', content)
        self.assertIn('Jantar', content)
