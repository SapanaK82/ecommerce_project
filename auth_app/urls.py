from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', signin_view, name='signin')
]
