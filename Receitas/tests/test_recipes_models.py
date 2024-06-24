from .test_recipes_base import ReceitasTestBase
from django.core.exceptions import ValidationError

class ReceitasModelsTest(ReceitasTestBase):
    
    def setUp(self) -> None:
        self.recipe = self.create_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70
        self.recipe.slug = 'A'

        with self.assertRaises(ValidationError):
            self.recipe.full_clean() # VALIDAÇÃO DO CAMPOS
