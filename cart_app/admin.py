from django.contrib import admin
from .models import CartItem
# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'user',
        'quantity',
        'price',
        'date_added'

    ]

admin.site.register(CartItem, CartItemAdmin)