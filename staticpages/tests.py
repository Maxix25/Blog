from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class HomepageTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username = 'testuser100', password = 'testpassword')
        self.client.login(username = 'testuser100', password = 'testpassword')

    def test_authenticated_navbar(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Settings')
    
    def test_unauthenticated_navbar(self):
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Login')