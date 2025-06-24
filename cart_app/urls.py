from django.urls import path
from .views import *



app_name = 'cart_app'

urlpatterns = [
    path('cart/', cart_view, name='cart_summery'),
    path('add/<pk>/', cart_add_view, name='cart_add'),
    path('update/', cart_update_view, name='cart_update'),
    path('delete/<pk>/', cart_delete_view, name='remove_item'),
    #path('cart_item/<pk>/', cart_create_view, name='cart_item')
]