from django import forms


class PostSearchForm(forms.Form):
  
    title = forms.CharField(
        max_length=255, required=False, label=('Post title'))
    author = forms.CharField(max_length=16, required=False, label=('Author'))

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['title'] = cleaned_data['title'].strip()
        cleaned_data['author'] = cleaned_data['author'].strip()
        return cleaned_data
