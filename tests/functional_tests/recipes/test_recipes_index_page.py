import pytest
from unittest import skip
from .base import RecipeBaseFunctionalTest
from unittest.mock import patch
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.functional_test
class RecipeIndexPageFunctionalTest(RecipeBaseFunctionalTest):

    @skip
    @patch('recipes.views.PER_PAGE', new=6)
    def test_the_test(self):
        self.create_recipe_in_batch(qtd=20)
        self.browser.get(self.live_server_url)
    
    def test_recipes_search_input_find_correct_recipe(self):
        recipes = self.create_recipe_in_batch(qtd=10)

        title_needed = 'Receita Foda'
        recipes[0].title = title_needed
        recipes[0].save()

        self.browser.get(self.live_server_url)
        search_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Procurar"]')
        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)
        self.assertIn(title_needed, self.browser.find_element(By.CLASS_NAME, 'main-content-list').text)
        self.sleep()
