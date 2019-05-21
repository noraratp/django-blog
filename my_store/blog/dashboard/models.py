from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    featured_image = models.ImageField(
        ("Featured Image"), upload_to=settings.OSCAR_IMAGE_FOLDER, max_length=255)
    post_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    excerpt = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
