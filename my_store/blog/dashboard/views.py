from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django_tables2 import SingleTableView
from django.views import generic
from django.urls import reverse

from .forms import PostSearchForm, PostForm
from .formsets import CategoryGroupFormSet
from .models import Post
from .tables import PostTable


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
            queryset = Post.objects.filter(
                author__email__icontains=data['author'])

        if data.get('title'):
            queryset = queryset.filter(title__icontains=data['title'])

        return queryset


class BlogCreateView(generic.CreateView):

    template_name = 'dashboard/blog/create.html'
    form_class = PostForm
    model = Post
    category_formset_class = CategoryGroupFormSet

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category_formset'] = self.category_formset_class(
            instance=self.object)
        return ctx

    def process_all_forms(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
        formset = self.category_formset_class(
            self.request.POST, instance=self.object)
        is_valid = form.is_valid() and formset.is_valid()
        print(form.errors)
        if is_valid:
            return self.forms_valid(form, formset)
        else:
            return self.forms_invalid(form, formset)

    form_valid = form_invalid = process_all_forms

    def forms_valid(self, form, formset):
        self.object = form.save()

        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def forms_invalid(self, form, formset):
        messages.error(self.request,
                       ("Your submitted data was not valid - please "
                        "correct the errors below"))
        context = self.get_context_data(form=form)
        context['category_formset'] = formset
        return self.render_to_response(context)

    def get_success_url(self):
        messages.success(self.request, ('Post created successfully'))

        action = self.request.POST.get('action')
        if action == 'continue':
            return reverse('blog:blog_detail_view', kwargs={'id': self.object.id})
        else:
            return reverse('blog:blog_list_view')


class BlogDetailView(generic.UpdateView):
    template_name = 'dashboard/blog/detail.html'
    form_class = PostForm
    context_object_name = 'post_detail'
    category_formset_class = CategoryGroupFormSet

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = self.form_class(instance=self.object)
        ctx['category_formset'] = self.category_formset_class(
            instance=self.object)
        return ctx

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['id'])

    def process_all_forms(self, form):
        formset = self.category_formset_class(
            self.request.POST, instance=self.object)
        is_valid = form.is_valid() and formset.is_valid()
        if is_valid:
            return self.forms_valid(form, formset)
        else:
            return self.forms_invalid(form, formset)

    form_valid = form_invalid = process_all_forms

    def forms_valid(self, form, formset):
        self.object = form.save()
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def forms_invalid(self, form, formset):
        messages.error(self.request,
                       ("Your submitted data was not valid - please "
                        "correct the errors below"))
        context = self.get_context_data(form=form)
        context['category_formset'] = formset
        return self.render_to_response(context)

    def get_success_url(self):

        action = self.request.POST.get('action')
        if action == 'continue':
            messages.success(self.request, ('save success'))
            url = reverse(
                'blog:blog_detail_view', kwargs={"id": self.object.id})
        elif action == 'save':
            messages.success(self.request, ('save success'))
            url = reverse('blog:blog_list_view')
        else:
            url = reverse('blog:blog_detail_view',
                          kwargs={"id": self.object.id})
        return url


class BlogDeleteView(generic.DeleteView):
    template_name = 'dashboard/blog/delete.html'
    model = Post
    context_object_name = 'posts'

    def get_success_url(self):
        messages.success(self.request, ('Post deleted successfully'))
        return reverse('blog:blog_list_view')
