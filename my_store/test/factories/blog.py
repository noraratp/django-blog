import factory
from datetime import datetime

from django.utils import timezone

from .category import CategoryFactory
from .user import UserFactory
from blog.dashboard.models import Post, PostCategory


class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: 'Hello Word {}'.format(n))
    content = factory.Sequence(lambda n: 'Hello Word Content {}'.format(n))
    post_date = datetime.now(tz=timezone.utc)
    author = factory.SubFactory(UserFactory)
    featured_image = factory.django.ImageField(color='blue')
    excerpt = "Test2"


class PostCategoryFactory(factory.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    post = factory.SubFactory(PostFactory)

    class Meta:
        model = PostCategory


class PostWithCategoryFactory(PostFactory):
    post_category_1 = factory.RelatedFactory(PostCategoryFactory, 'post')
    post_category_2 = factory.RelatedFactory(PostCategoryFactory, 'post')
