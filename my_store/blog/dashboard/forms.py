from oscar.forms.widgets import DateTimePickerInput

from django import forms

from .models import Post, PostCategory, Category


class PostSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255, required=False, label=('Post title'))
    author = forms.CharField(max_length=16, required=False, label=('Author'))

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['title'] = cleaned_data['title'].strip()
        cleaned_data['author'] = cleaned_data['author'].strip()

        return cleaned_data


class PostForm(forms.ModelForm):

    post_date = forms.DateTimeField(widget=DateTimePickerInput())

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'featured_image', 'author', 'excerpt', 'post_date')


class CategoryGroupForm(forms.ModelForm):

    class Meta:
        model = PostCategory
        fields = ['category', 'post']


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class CategorySearchForm(forms.Form):
    name = forms.CharField(required=False, label=("Name"))

    class Meta:
        fields = ['name']

    def clean(self):
        cleaned_data = super(CategorySearchForm, self).clean()
        cleaned_data['name'] = cleaned_data['name']
        return cleaned_data
