from django.test import TestCase

from blog.dashboard.forms import PostSearchForm


class TestPostSearchForm(TestCase):
    def setUp(self):
        self.form = PostSearchForm

    def test_clean_should_return_correctly_data(self):
        data = {'title': ' Test Title ', 'author': ' pich@29next.com '}
        form = self.form(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['title'], 'Test Title')
        self.assertEqual(form.cleaned_data['author'], 'pich@29next.com')
