
from django.urls import path
from .views import *

urlpatterns = [
    path('user/form/', user_create_view, name='user_url'),
    path('user/show/', user_retrieve_view, name='show_user'),   
    path('artist/form/', artist_create_view, name = 'artist_url'),
    path('artist/show/', artist_retrieve_view, name = 'show_artist')
]