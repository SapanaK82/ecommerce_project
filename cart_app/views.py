from django.shortcuts import render, redirect
from .models import CartItem
from product_app.models import Product


# Create your views here.


def cart_view(request):
    cart_items = CartItem.objects.filter(user = request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    template_name = 'cart_app/cart_summery.html'
    context =  {'cart_items': cart_items, 'total_price': total_price}
    return render(request, template_name, context)

def cart_add_view(request, pk):
    product = Product.objects.get(id=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_app:cart_summery')


def cart_update_view(request):
    pass

def cart_delete_view(request, pk):
    cart_item = CartItem.objects.get(id=pk)
    cart_item.delete()
    return redirect('cart_app:cart_summery') 
    