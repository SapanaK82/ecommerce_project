
from django.urls import path
from .views import *

urlpatterns = [
    path('category/form/', category_create_view, name='category'),
    path('category/show/', category_retrieve_view, name='show_category'),
]