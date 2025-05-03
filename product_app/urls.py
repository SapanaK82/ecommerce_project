from django.urls import path
from .views import *

urlpatterns = [
    path('product/form/', product_create_view, name='product'),
    path('single_prodcut/<pk>/', product_retrieve_view, name='single_product'),
    path('update_product/<pk>/', product_update_view, name='update_product'),
    path('delete_product/<pk>/', product_delete_view, name='delete_product'),
    path('product_image/', product_show_view, name='product_image'),
]