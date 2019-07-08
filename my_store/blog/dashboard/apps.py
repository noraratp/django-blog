from oscar.core.application import Application

from django.conf.urls import url

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView


class BlogApplication(Application):
    name = 'blog'
    label = 'blog_list'
    verbose_name = ('Blog')

    default_permissions = ['is_staff', ]
    blog_list_view = BlogListView
    blog_detail_view = BlogDetailView
    blog_create_view = BlogCreateView
    blog_delete_view = BlogDeleteView

    def get_urls(self):
        urls = [
            url(r'^blog-list-view/$', self.blog_list_view.as_view(),
                name='blog-list-view'),
            url(r'^blog-list-view/post/create/$',
                self.blog_create_view.as_view(),
                name='blog-create-view'),
            url(r'^blog-list-view/(?P<id>\d+)/$',
                self.blog_detail_view.as_view(),
                name='blog-detail-view'),
            url(r'^delete/(?P<pk>\d+)/$',
                self.blog_delete_view.as_view(),
                name='blog-detail-delete-view'),
        ]
        return self.post_process_urls(urls)


application = BlogApplication()
