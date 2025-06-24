
from django.urls import path
from .views import *

urlpatterns = [
    path('user/form/', register_view, name='user_url'),
    
    path('signin/', signin_view, name='signin'),
    path('logout/', logout_view, name='logout'),
    #path('forgot/password/<pk>/', username_password_view, name='forgot_pw'),

    path('user/show/', user_retrieve_view, name='show_user'),  
    path('user/update/<pk>/', user_update_view, name='update_user'),  
    path('user/delete/<pk>/', user_delete_view, name='delete_user'), 
    path('dashboard/<pk>/', user_dashboard, name='dashboard'),


    path('artist/form/', artist_create_view, name = 'artist_url'),
    path('artist/show/', artist_retrieve_view, name = 'show_artist'),
    path('artist_page/<pk>/', artist_page_view, name='artist_page'),
    path('artist_update/<pk>/', artist_update_view, name='artist_update'),
    path('artist_delete/<pk>/', artist_delete_view, name='artist_delete'),

]