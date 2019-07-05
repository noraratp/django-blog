import tempfile

from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from blog.dashboard.models import Post
from test.factories import PostFactory, CategoryFactory


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


class TestBlogCreateView(WebTestCase):
    def setUp(self):
        self.url = reverse('blog:blog_create_view')
        self.category_factory = CategoryFactory()

    def test_form_model_should_equal_Post(self):
        self.assertEquals(self.form.Meta.model, Post)

    def test_get_view_should_return_status_code_200(self):
        self.login_with_staff_user()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_create_post_model_should_store_correctly_data(self):
        self.login_with_staff_user()
        data = {
            'title': 'Test title post',
            'content': 'test content',
            'author': self.user.id,
            'excerpt': 'example excerpt',
            'post_date': datetime.now(tz=timezone.utc),
            'featured_image': tempfile.NamedTemporaryFile(suffix=".jpg").name,
            'postcategory_set-TOTAL_FORMS': ['3'],
            'postcategory_set-INITIAL_FORMS': ['0'],
            'postcategory_set-MIN_NUM_FORMS': ['1'],
            'postcategory_set-MAX_NUM_FORMS': ['1000'],
            'postcategory_set-0-category': ['1'],
            'postcategory_set-0-post': [''],
            'postcategory_set-0-id': [''],
            'postcategory_set-1-category': [''],
            'postcategory_set-1-post': [''],
            'postcategory_set-1-id': [''],
            'postcategory_set-2-category': [''],
            'postcategory_set-2-post': [''],
            'postcategory_set-2-id': [''],
        }

        response = self.client.post(
            self.url, data=data)
        self.assertEqual(response.status_code, 302)
        print(response.status_code)
        # expect_post = Post.objects.all().get(title=data['title'])
        # self.assertEqual(expect_post.content, data['content'])
        # self.assertEqual(expect_post.author, self.user)
        # self.assertEqual(expect_post.excerpt, data['excerpt'])

        # expect_post = Post.objects.all()
        print(Post.objects.all())

        # self.assertEqual(expect_post.content, data['content'])
        # self.assertEqual(expect_post.author, self.user)
        # self.assertEqual(expect_post.excerpt, data['excerpt'])


# class TestlUpdateView(WebTestCase):

#     def setUp(self):
#         self.post_factory = PostFactory()
#         self.category_factory = CategoryFactory()
#         self.url_post_detail_view = reverse(
#             'blog:blog_create_view',
#             kwargs={'id': self.post_factory.id}
#         )

#     def test_response_status_code_update_view_should_equal_200(self):
#         self.login()
#         response_client = self.client.get(self.url_post_detail_view)
#         self.assertEqual(response_client.status_code, 200)

#     def test_detail_should_have_data_we_expect(self):
#         self.login()
#         response_client = self.client.get(self.url_post_detail_view)
#         self.assertEqual(response_client.context['post'], self.post_factory)

#     def test_post_detail_update_view_should_update_data_in_db(self):
#         self.login()
#         data = {
#             'title': 'Test update post',
#             'content': 'example content',
#             'author': self.user.id,
#             'excerpt': 'example excerpt',
#             'post_date': '2018-03-12',
#             'featured_image': tempfile.NamedTemporaryFile(suffix=".jpg").name,
#             'postcategory_set-TOTAL_FORMS': '2',
#             'postcategory_set-INITIAL_FORMS': '0',
#             'postcategory_set-MIN_NUM_FORMS': '1',
#             'postcategory_set-0-category': self.category_factory.id
#         }

#         response = self.client.post(self.url_post_detail_view, data=data)
#         self.assertEqual(response.status_code, 302)

#         expect_data = Post.objects.get(id=self.post_factory.id)
#         self.assertEqual(expect_data.content, data['content'])
#         self.assertEqual(expect_data.author, self.user)
#         self.assertEqual(expect_data.excerpt, data['excerpt'])
#         # self.assertQuerysetEqual(
#         #     expect_data.abstractcategorygroup_set.all().filter(
#         #         post__title=data['title']),
#         #     ['<AbstractCategoryGroup: {}-{}>'.format(expect_data, self.category_factory)])
