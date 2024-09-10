from time import sleep
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from sources.browser import create_chrome_browser
from recipes.tests.test_recipes_base import RecipeMixin

class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixin):

    def setUp(self) -> None:
        self.browser = create_chrome_browser('--headless')
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        sleep(seconds)
