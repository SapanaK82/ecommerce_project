from django.urls import path
from .views import *

urlpatterns = [
    path('product/form/', product_create_view, name='product'),

    path('single_product/<int:pk>/', product_retrieve_view, name='single_product'),
    path('update_product/<int:pk>/', product_update_view, name='update_product'),
    path('delete_product/<int:pk>/', product_delete_view, name='delete_product'),
    path('product_image/', product_show_view, name='product_image'),


    path('review/<product_id>/', product_review, name='product_review'),
    path('show/review/<int:pk>/', show_review, name='show_review'),
    path('delete/review/<int:pk>/', delete_review, name='delete_review'),
    path('customer/review/<int:pk>/', customer_review, name='customer_review'),


]