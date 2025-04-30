from .models import Product, ProductImage
from django import forms



class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        labels = {
            'artist' : 'ARTIST',
            'pname' : 'PRODUCT NAME',
            'description' : 'DESCRIPTION',
            'price' : 'PRICE',
            'material' : 'MATERIAL',
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