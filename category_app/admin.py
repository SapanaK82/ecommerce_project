from django.contrib import admin

from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'description', 'created_at']


admin.site.register(Category, CategoryAdmin)