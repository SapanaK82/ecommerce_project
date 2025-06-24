from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomUser, Artist
# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'contact_number', 'address', 'is_artist')

admin.site.register(CustomUser, CustomUserAdmin)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'photo', 'category', 'Address', 'rating', 'created_at')

admin.site.register(Artist, ArtistAdmin)