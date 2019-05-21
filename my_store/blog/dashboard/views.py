# from django.shortcuts import render
from .models import Post
from django.views import generic

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


class BlogListView(generic.ListView):
    template_name = 'dashboard/blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.all()
