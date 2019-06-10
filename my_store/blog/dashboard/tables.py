from .models import Post
import django_tables2 as tables


class PostTable(tables.Table):

    author = tables.TemplateColumn('{{ record.author.email | default:"-" }}')

    class Meta:
        model = Post
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'title', 'content', 'author', 'category', 'excerpt')
