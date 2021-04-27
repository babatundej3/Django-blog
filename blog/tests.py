from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .model import Post

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user =get_user_model().objects.create_user(
            username= 'tboy'
            email='tboy@gmail.com'
            password='boyscott'
        )

        self.post = Post.objects.create(
            title='Beauty',
            body='Beauty is vein'
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Beauty')
        self.assertEqual(f'{self.post.author}', 'tboy')
        self.assertEqual(f'{self.post.body}', 'Beauty is vien')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Beauty is vien')
        self.assertTemplateUsed(response, 'home,html')

    def test_post_detail_views(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 480)
        self.assertContains(response, 'Beauty')
        self.assertTemplateUsed(response, 'post_detail.html')

