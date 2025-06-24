# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from product_app.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')  # Redirect to wishlist page

@login_required
def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('wishlist')

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist_app/wishlist.html', {'wishlist_items': wishlist_items})
