from django import forms
from .models import Category


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        labels = {
            'category_name' : 'CATEGORY NAME',
            'description' : 'DESCRIPTION',
            'created_at' : 'CREATED_AT'
        }