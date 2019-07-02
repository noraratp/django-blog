from oscar.core.application import Application
from .views import BlogListView, BlogDetailView, BlogCreateView
from django.conf.urls import url


class BlogApplication(Application):
    name = 'blog'
    label = 'blog_list'
    verbose_name = ('Blog')

    default_permissions = ['is_staff', ]
    blog_list_view = BlogListView
    blog_detail_view = BlogDetailView
    blog_create_view = BlogCreateView

    def get_urls(self):
        urls = [
            url(r'^blog_list_view/$', self.blog_list_view.as_view(),
                name='blog_list_view'),
            url(r'^blog_list_view/post/create/$',
                self.blog_create_view.as_view(),
                name='blog_create_view'),
            url(r'^blog_list_view/(?P<pk>\d+)/$',
                self.blog_detail_view.as_view(),
                name='blog_detail_view'),
            
            
        ]
        return self.post_process_urls(urls)


application = BlogApplication()
