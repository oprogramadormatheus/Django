from unittest import skip
from .test_recipes_base import ReceitasTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized

class ReceitasModelsTest(ReceitasTestBase):
    
    def setUp(self) -> None:
        self.recipe = self.create_recipe()
        return super().setUp()

    @skip('Just a Test')
    def test_recipe_title_field_max_length(self):
        self.recipe.title = 'A' * 70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand([('title', 65), ('description', 165), ('preparation_time_unit', 65), ('servings_unit', 65)])
    def test_recipe_fields_max_length(self, field, size):
        setattr(self.recipe, field, 'A' * (size + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean() # VALIDAÇÃO DO CAMPOS
