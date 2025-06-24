from django.contrib import admin
from .models import Product, ProductReview
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['artist',
            'pname',
            'description',
            'price',
            'medium',
            'weight',
            'dimensions',
            'COLOR_CHOICES',
            'color',
            'STYLE_CHOICES',
            'style',
            'category',
            'images',
            'is_bestseller',
            'created_at']

admin.site.register(Product, ProductAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display =[
        'product',
        'created_by',
        'title',
        'content',
        'created_at',
]

admin.site.register(ProductReview, ProductReviewAdmin)