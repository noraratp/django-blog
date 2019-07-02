from oscar.core.application import Application

from django.conf.urls import url

from .views import BlogListView


class BlogApplication(Application):
    name = 'blog'
    label = 'blog_list'
    verbose_name = ('Blog')

    default_permissions = ['is_staff', ]
    blog_list_view = BlogListView

    def get_urls(self):
        urls = [
            url(r'^blog_list_view/$', self.blog_list_view.as_view(),
                name='blog_list_view')
        ]
        return self.post_process_urls(urls)


application = BlogApplication()
