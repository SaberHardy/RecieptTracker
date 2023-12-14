from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class MembersTestCase(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.test_user = User.objects.create_user(
            username='testuser',
            password='testpassword12345'
        )

    def test_login_user_view(self):
        # Test the login view with valid credentials
        response = self.client.post(reverse('login_user'), {'username': 'testuser', 'password': 'testpassword12345'})
        self.assertEqual(response.status_code, 200)  # Check if the response is a redirect
        self.assertRedirects(response, reverse('index'))

        # Test the login view with invalid credentials
        response = self.client.post(reverse('login_user'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('login_user'))

    def test_register_user_view(self):
        # Test the register view with valid data
        response = self.client.post(reverse('register_user'),
                                    {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('index'))

        # Test the register view with invalid data
        response = self.client.post(reverse('register_user'),
                                    {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertEqual(response.status_code,
                         200)  # Check if the response is a success (200) status for a failed form submission
        self.assertContains(response, 'A user with that username already exists.')

    def test_logout_user_view(self):
        # Login the test user before testing logout
        self.client.login(username='testuser', password='testpassword')

        # Test the logout view
        response = self.client.get(reverse('logout_user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

        # Check if the user is logged out
        response = self.client.get(reverse('index'))
        self.assertNotContains(response, 'testuser')  # Check if the username is not present in the response content
