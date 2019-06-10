from .models import Post
from .tables import PostTable
from .forms import PostSearchForm
from django_tables2 import SingleTableView


class BlogListView(SingleTableView):
    template_name = 'dashboard/blog/index.html'
    form_class = PostSearchForm
    context_object_name = 'latest_post_list'
    table_class = PostTable
    context_table_name = 'post_table'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = self.form
        return ctx

    def get_queryset(self):
        queryset = Post.objects.all()
        queryset = self.apply_search(queryset)
        return queryset

    def apply_search(self, queryset):

        self.form = self.form_class(self.request.GET)

        if not self.form.is_valid():
            return queryset

        data = self.form.cleaned_data
        if data.get('author'):
            queryset = Post.objects.filter(author__email__icontains=data['author'])

        if data.get('title'):
            queryset = queryset.filter(title__icontains=data['title'])

        return queryset
