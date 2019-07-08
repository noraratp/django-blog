from oscar.core.compat import AUTH_USER_MODEL

from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    featured_image = models.ImageField(
        ("Featured Image"), upload_to=settings.OSCAR_IMAGE_FOLDER, max_length=255, blank=True)
    post_date = models.DateTimeField('date published')
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name=("Author"))
    category = models.ManyToManyField(Category, through='PostCategory')
    excerpt = models.CharField(max_length=200)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.category, self.post.title)
