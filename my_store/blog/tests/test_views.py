from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone


from test.factories import PostFactory


class WebTestCase(TestCase):
    username = 'admin'
    password = 'top12345'

    def login_with_staff_user(self):
        self.user = User.objects.create(username=self.username)
        self.user.set_password(self.password)
        self.user.is_staff = True
        self.user.save()

        self.client = Client()
        self.client.login(
            username=self.username,
            password=self.password
        )


class TestBlogListView(WebTestCase):
    def setUp(self):
        self.url = reverse('blog:blog_list_view')
        self.post_1 = PostFactory(
            title='xxxxxxxxx', post_date=timezone.now()+timedelta(days=30))
        self.post_2 = PostFactory(
            title='yyyyyyyyyy', post_date=timezone.now()+timedelta(days=31), author__email="test@29next.com")
        self.post_3 = PostFactory(
            title='three post', post_date=timezone.now()+timedelta(days=32), author__email="pich1@29next.com")

    def test_get_view_should_return_status_code_200(self):
        self.login_with_staff_user()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_get_context_data_should_return_data(self):
        self.login_with_staff_user()
        response = self.client.get(self.url)

        expected_data = [
            '<Post: {}>'.format(self.post_3),
            '<Post: {}>'.format(self.post_2),
            '<Post: {}>'.format(self.post_1)
        ]
        self.assertQuerysetEqual(
            response.context['post_table'].data.data, expected_data)

    def test_search_with_author_should_return_correctly_data(self):
        self.login_with_staff_user()
        url = self.url + '{}'.format("?author=pich1@29next.com")
        response = self.client.get(url)

        expected_data = [
            '<Post: {}>'.format(self.post_3),
        ]
        self.assertQuerysetEqual(
            response.context['post_table'].data.data, expected_data)

    def test_search_with_title_should_return_correctly_data(self):
        self.login_with_staff_user()
        url = self.url + '{}'.format("?title=xxxxxxxx")
        response = self.client.get(url)

        expected_data = [
            '<Post: {}>'.format(self.post_1),
        ]
        self.assertQuerysetEqual(
            response.context['post_table'].data.data, expected_data)

    def test_search_with_title_and_author_should_return_correctly_data(self):
        self.login_with_staff_user()
        url = self.url + '{}'.format("?title=yyyyyy&author=test@29next.com")
        response = self.client.get(url)
        expected_data = [
            '<Post: {}>'.format(self.post_2),
        ]
        self.assertQuerysetEqual(
            response.context['post_table'].data.data, expected_data)
