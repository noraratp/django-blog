from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    featured_image = models.CharField(max_length=200)
    post_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    # category = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
