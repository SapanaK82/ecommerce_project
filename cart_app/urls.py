from django.urls import path
from .views import *

urlpatterns = [
    path('cart_item/<pk>/', cart_create_view, name='cart_item')
]