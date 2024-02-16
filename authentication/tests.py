from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class AuthenticationTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'testuser200',
            password = 'testpassword', 
            email = 'djangotestuser@test.com'
        )

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': self.user.username,
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
    
    def test_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'othertestuser',
            'email': 'somerandomemail@email.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, "Account created succesfully, you may now login")
    
    def test_logout(self):
        self.client.login(username = self.user.username, password = 'testpassword')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        self.assertFalse(self.client.session.get('_auth_user_id'))

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'testuser200',
            password = 'testpassword'
        )
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout'), follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, "Logged out succesfully!")