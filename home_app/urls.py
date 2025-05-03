from django.urls import path
from .views import *

urlpatterns = [
    #path('', home_view, name='home'),
    path('', product_show_view, name='home')
]