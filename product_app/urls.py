from django.urls import path
from .views import *

urlpatterns = [
    path('product/form/', product_create_view, name='product'),
    path('show_product/', product_show_view, name='show_product')
]