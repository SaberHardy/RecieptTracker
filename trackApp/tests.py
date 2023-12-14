from django.test import TestCase, Client
from django.urls import reverse
from trackApp.models import Recipe
from django.urls import reverse
from django.contrib.auth.models import User


# class ListItemsTestCase(TestCase):
#     def setUp(self):
#         # Create some test data (recipes) for the view
#         Recipe.objects.create(user_id=23,
#                               store_name='Recipe 1',
#                               date_of_purchase='2023-12-31',
#                               price=100, quantity=10)
#
#         Recipe.objects.create(user_id=12,
#                               store_name='Recipe 2',
#                               date_of_purchase='2023-10-10',
#                               price=100,
#                               quantity=12)
#
#     def test_list_items_view(self):
#         # Create a test client
#         client = Client()
#
#         # Make a GET request to the view
#         response = client.get(reverse('index'))
#
#         # Check that the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)
#
#         # Check that the rendered context contains the expected data
#         self.assertQuerysetEqual(
#             response.context['all_recipes'],
#             ['<Recipe: Recipe 2>', '<Recipe: Recipe 1>'],
#             ordered=True
#         )
#
#         # Check that the response contains the rendered template
#         self.assertTemplateUsed(response, 'trackApp/index.html')


class RecipeModelTestCase(TestCase):
    def setUp(self):
        # Create a test user for the Recipe model
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def test_recipe_model_methods(self):
        # Create a Recipe instance
        self.recipe = Recipe.objects.create(
            user=self.test_user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item='Test Item',
            price=10.0,
            quantity=2,
            status='Ordered'
        )

        # Test calculate_total_amount method
        self.assertEqual(self.recipe.calculate_total_amount(), 20.0)  # 2 (quantity) * 10.0 (price)

        # Test get_absolute_url method
        expected_url = reverse('index')
        self.assertEqual(self.recipe.get_absolute_url(), expected_url)

        # Test save and delete methods
        recipe_id = self.recipe.id
        # Save the Recipe instance
        self.recipe.save()
        # Check if the save method logs the correct message
        with self.assertLogs('trackApp.models', level='INFO') as log_messages:
            self.recipe.save()
            self.assertIn(f"Saving Recipe instance with ID {recipe_id}", log_messages.output[0])

        # Delete the Recipe instance
        self.recipe.delete()
        # Check if the delete method logs the correct message
        with self.assertLogs('trackApp.models', level='INFO') as log_messages:
            self.recipe.delete()
            self.assertIn(f"Deleting Recipe instance with ID {recipe_id}", log_messages.output[0])

    def test_recipe_model_str_method(self):
        # Create a Recipe instance
        recipe = Recipe.objects.create(
            user=self.test_user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item='Test Item',
            price=10.0,
            quantity=2,
            status='Ordered'
        )

        # Test __str__ method
        expected_str = f"Test Store - 2023-01-01"
        self.assertEqual(str(recipe), expected_str)
