from django.forms import Form,ModelChoiceField,Select
from .models import Category,Product


class formSelect(Form):
    category = ModelChoiceField(queryset=Category.objects.all(),widget=Select(
        attrs={'class': 'form-control select2'}
    ))
    product = ModelChoiceField(queryset=Product.objects.none(),widget=Select(
        attrs={'class': 'form-control select2'}
    ))