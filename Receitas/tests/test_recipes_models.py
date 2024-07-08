from unittest import skip
from .test_recipes_base import ReceitasTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized

class ReceitasModelsTest(ReceitasTestBase):
    
    def setUp(self) -> None:
        self.recipe = self.create_recipe()
        return super().setUp()
    
    def create_recipe_no_defaults(self, slug):

        recipe_test = Recipe.objects.create(
            category = self.create_category(name='Test Default Category'),
            author = self.create_author(username='test.user'),
            title = 'Test Title',
            description = 'Test Description',
            slug = slug,
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Pessoas',
            preparation_steps = 'Test Preparation Steps',
        )
        recipe_test.full_clean()
        recipe_test.save()
        return recipe_test
    
    @skip('WIP')
    def test_recipe_title_field_max_length(self):
        self.recipe.title = 'A' * 70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand([('title', 65), ('description', 165), ('preparation_time_unit', 65), ('servings_unit', 65)])
    def test_recipe_fields_max_length(self, field, size):
        setattr(self.recipe, field, 'A' * (size + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_if_false_by_default(self):
        recipe_test = self.create_recipe_no_defaults('slug-test-1')
        self.assertFalse(recipe_test.preparation_steps_is_html)

    def test_recipe_is_published_is_false_by_default(self):
        recipe_test = self.create_recipe_no_defaults('slug-test-2')
        self.assertFalse(recipe_test.is_published)

    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = 'Testing Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), needed, 
            msg=f'Recipe string representation should be "{needed}", but was "{str(self.recipe)}"')
    
    def test_recipe_category_model_string_representation(self):
        self.category = self.create_category(name='Category Testing')
        self.assertEqual(str(self.category), self.category.name)
    
    def test_recipe_category_model_name_field_max_length(self):
        name = 'A' * 70
        self.category = self.create_category(name=name)
        with self.assertRaises(ValidationError):
            self.category.full_clean()
