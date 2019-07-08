from django.test import TestCase

from blog.dashboard.forms import PostSearchForm, PostForm
from blog.dashboard.models import Post
from test.factories.blog import UserFactory


from .util import Util


class TestPostSearchForm(TestCase):
    def setUp(self):
        self.form = PostSearchForm

    def test_clean_should_return_correctly_data(self):
        data = {'title': ' Test Title ', 'author': ' pich@29next.com '}
        form = self.form(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['title'], 'Test Title')
        self.assertEqual(form.cleaned_data['author'], 'pich@29next.com')


class TestPostForm(TestCase):
    def setUp(self):
        self.form = PostForm
        self.util = Util()
        self.user = UserFactory()

    def test_form_model_should_equal_Post(self):
        self.assertEquals(self.form.Meta.model, Post)

    def test_should_have_fields_that_we_expect(self):
        expected_fields = ('id', 'title', 'content',
                           'featured_image',  'author', 'excerpt', 'post_date')
        self.assertEquals(expected_fields, self.form.Meta.fields)

    def test_required_fields_have_not_data(self):
        data = {}

        form = self.form(data=data)
        self.assertFalse(form.is_valid())

        expected_errors = {
            'author': ['This field is required.'],
            'excerpt': ['This field is required.'],
            'title': ['This field is required.'],
            'post_date': ['This field is required.'],
        }

        self.assertDictEqual(form.errors, expected_errors)

    def test_post_form_save_data_should_have_data_in_db(self):

        data = {
            'title': 'Title Test Post',
            'content': 'test content',
            'author': self.user.id,
            'excerpt': 'example excerpt',
            'post_date': '2018-03-12',
        }
        form = self.form(data)
        form.is_valid()
        self.assertTrue(form.is_valid())
        form.save()
        post = Post.objects.get(title=data['title'])
        self.assertEqual(post.content, data['content'])
        self.assertEqual(post.excerpt, data['excerpt'])
