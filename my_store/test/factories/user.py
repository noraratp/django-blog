import factory

from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    username = factory.Sequence(lambda n: 'username_{}'.format(n))
    password = 'password'
    email = factory.Sequence(lambda x: 'pich{}@29next.com'.format(x))
