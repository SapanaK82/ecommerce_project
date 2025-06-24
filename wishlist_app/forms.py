from .models import Wishlist
from django import forms

class WishlistModelForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = '__all__'
