from .models import Product, ProductImage, ProductReview
from django import forms



class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['artist']

        labels = {
            'artist' : 'ARTIST',
            'pname' : 'PRODUCT NAME',
            'description' : 'DESCRIPTION',
            'price' : 'PRICE',
            'medium' : 'MEDIUM',
            'weight' : ' WEIGHT',
            'dimensions' : 'DIMENSIONS',
            'COLOR_CHOICES' : 'COLOR_CHOICES',
            'color' : 'COLOR',
            'STYLE_CHOICES' : 'STYLE_CHOICES',
            'style' : 'STYLE',
            'category' : 'CATEGORY',
            'images' : 'IMAGES',
            'is_bestseller' : 'IS BESTSELLER',
            'created_at' : 'CREATED AT'
        }


class ProductImageModelForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'

        labels = {
            'product' : 'PRODUCT',
            'image_url' : 'IMAGE URL'
        }

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('title', 'content',)
