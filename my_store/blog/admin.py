from django.contrib import admin
from .dashboard.models import Post, Category, PostCategory

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
