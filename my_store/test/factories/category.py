import factory

from blog.dashboard.models import Category


class CategoryFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Category %d' % n)

    class Meta:
        model = Category
