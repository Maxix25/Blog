import os
from django.contrib.staticfiles import finders
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = 'testuser', password = 'testpassword')
        self.profile = Profile.objects.get(user = self.user)
    
    def test_profile_image_url(self):
        self.assertEqual(self.profile.image.url, settings.STATIC_URL + 'profile_pics/default.jpeg')
    
    def test_primary_key(self):
        self.assertEqual(self.user, self.profile.user)



class SettingsPageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_settings_page_view(self):
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)

    def test_settings_page_view_post(self):
        # Create a temporary image file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Get the absolute path of the file in the static folder of your app
        absolute_path = os.path.join(base_dir, 'static', 'profile_pics', self.user.username, 'resume.png')
        with open(absolute_path, 'rb') as img:
            response = self.client.post(reverse('settings'), {
                'username': 'newusername',
                'email': 'newemail@example.com',
                'bio': 'This is a new bio',
                'image': SimpleUploadedFile('image.jpg', img.read())
            })
        self.assertEqual(response.status_code, 302)  # Redirect expected
        self.assertEqual(User.objects.get(username='newusername').email, 'newemail@example.com')
        self.assertEqual(Profile.objects.get(user=self.user).bio, 'This is a new bio')
        self.assertTrue(Profile.objects.get(user=self.user).image)

    def test_settings_page_view_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?next=/profile/settings/')
