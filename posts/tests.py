from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Posts
from user_profile.models import Profile

class PostsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Test Author',
            password = make_password("some password"),
            email = "someemail@email.com"
        )
        self.profile = Profile.objects.get(user = self.user)
        self.post = Posts.objects.create(
            author=self.profile,
            content='A',
            date='2024-02-04',
            topic='Python'
        )

    def test_post_detail_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('view_post', args=[self.post.id]))
        self.assertIn(response.status_code, [200, 302])
        self.assertContains(response, self.post.content)

    def test_post_create_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('create_post'), {
            'author': self.profile,
            'title': 'Test title',
            'content': 'B',
            'topic': 'PYTHON'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Posts.objects.all().order_by('-content')[0].content, 'B')

    # Add more test cases as needed
