# from django.shortcuts import render
from .models import Post
from django_tables2 import SingleTableView
from .tables import PostTable
from .forms import PostSearchForm

# Create your views here.
# class PostListView(SingleTableView):
#     template_name = 'oscar/dashboard/catalogue/category_list.html'
#     table_class = CategoryTable
#     context_table_name = 'categories'

#     def get_queryset(self):
#         return Category.get_root_nodes()

#     def get_context_data(self, *args, **kwargs):
#         ctx = super().get_context_data(*args, **kwargs)
#         ctx['child_categories'] = Category.get_root_nodes()
#         return ctx


class BlogListView(SingleTableView):
    template_name = 'dashboard/blog/index.html'
    form_class = PostSearchForm
    context_object_name = 'latest_post_list'
    table_class = PostTable
    context_table_name = 'post_table'    

    def get_context_data(self, **kwargs):        
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = self.form
        print("get_context_data")
        return ctx

    def get_queryset(self):
        print("get_queryset")
        queryset = Post.objects.all()
        queryset = self.apply_search(queryset)
        return queryset

    def apply_search(self, queryset):
        print("apply_search")
        """
        Search through the filtered queryset.

        We must make sure that we don't return search results that the user is not allowed
        to see (see filter_queryset).
        """
        self.form = self.form_class(self.request.GET)

        if not self.form.is_valid():
            return queryset

        data = self.form.cleaned_data

        if data.get('author'):
            queryset = Post.objects.filter(author__icontains=data['author'])
            print("Author :", queryset)

        if data.get('title'):
            queryset = queryset.filter(title__icontains=data['title'])
            print("Title :", queryset)

        return queryset
