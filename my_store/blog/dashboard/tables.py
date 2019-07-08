import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor


from .models import Post


class PostTable(tables.Table):

    author = tables.TemplateColumn('{{ record.author.email | default:"-" }}')

    title = tables.LinkColumn('blog:blog-detail-view', args=[A('pk')])

    actions = tables.TemplateColumn(
        verbose_name=('Actions'),
        template_name='dashboard/blog/blog_row_actions.html',
        orderable=False)

    class Meta:
        model = Post
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'title', 'content', 'author', 'category', 'excerpt')
