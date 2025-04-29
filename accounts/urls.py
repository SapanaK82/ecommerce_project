
from django.urls import path
from .views import *

urlpatterns = [
    path('user/form/', user_view, name='user_url'),
    path('artist/form/', artist_view, name = 'artist_url')
]