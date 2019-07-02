from django.forms.models import inlineformset_factory

from .forms import CategoryGroupForm
from .models import Post, PostCategory


CategoryGroupFormSet = inlineformset_factory(
    Post, PostCategory, form=CategoryGroupForm, extra=2, min_num=1, can_delete=True)
