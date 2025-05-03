from django.shortcuts import render
from .models import CartItem
from product_app.models import Product
# Create your views here.


def view_cart(request):
    cart_items = CartItem.objects.filter(user = request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    template_name = 'cart_app/cart.html'
    context =  {'cart_items': cart_items, 'total_price': total_price}
    return render(request, template_name, context)

def cart_create_view(request, pk):
    product = Product.objects.get(id=pk)
    cart_item = CartItem.objects.get(product=product, user = request.user) 
    #cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    template_name = 'cart_app/cart.html'
    context = {'cart_item': cart_item}
    return render(request, template_name, context)