import django_tables2 as tables
from .models import Post
# from django_tables2 import A, Column, TemplateColumn


class PostTable(tables.Table):
    class Meta:
        model = Post
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'title', 'content', 'author', 'category', 'excerpt')
