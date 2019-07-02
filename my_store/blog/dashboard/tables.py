from .models import Post
import django_tables2 as tables


class PostTable(tables.Table):

    author = tables.TemplateColumn('{{ record.author.email | default:"-" }}')

    title = tables.TemplateColumn(
        verbose_name=('Title'),
        template_name='dashboard/blog/blog_row_title.html',
        order_by='title', accessor=('title'))

    actions = tables.TemplateColumn(
        verbose_name=('Actions'),
        template_name='dashboard/blog/blog_row_actions.html',
        orderable=False)

    class Meta:
        model = Post
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'title', 'content', 'author', 'category', 'excerpt')
