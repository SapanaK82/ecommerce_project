from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductModelForm, ProductImageModelForm, ReviewModelForm
from .models import Product, ProductImage, ProductReview
from accounts.models import Artist
from django.db.models import Q
from django.http import HttpResponseForbidden

# Create your views here.
def product_create_view(request):
    form = ProductModelForm()
    if request.method=='POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.artist = Artist.objects.get(user=request.user)
            product.save()
            return redirect('home')
    template_name = 'product_app/product_form.html'
    context = {'form':form}
    return render(request, template_name, context)


#all product retrieve view

def product_show_view(request):
    products = Product.objects.all()
    styles = request.GET.getlist('style')
    materials = request.GET.getlist('material')
    price_ranges = request.GET.getlist('price')

    if styles:
        products = products.filter(style__in=styles)

    if materials:
        products = products.filter(material__in=materials)

    if price_ranges:
        price_query = Q()
        for pr in price_ranges:
            min_price, max_price = pr.split('-')
            price_query |= Q(price__gte=min_price, price__lte=max_price)
        products = products.filter(price_query)

    return render(request, 'home.html', {'products': products})


#to update a prodcut

def product_update_view(request, pk):
    obj = Product.objects.get(id=pk)
    form = ProductModelForm(instance=obj)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'product_app/product_form.html'
    context = {'form':form}
    return render(request, template_name, context)


#single product retrieve view

def product_retrieve_view(request, pk):
    obj = Product.objects.get(id=pk)
    template_name = 'product_app/single_product.html'
    context = {'data':obj}
    return render(request, template_name, context)


#product delete view

def product_delete_view(request, pk):
    obj = Product.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    template_name = 'product_app/delete_product.html'
    context = {'data':obj}
    return render(request, template_name, context)



def product_image_view(request):
    form = ProductImageModelForm()
    if request.method == 'POST':
        form = ProductImageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    template_name = 'product_app/product_image.html'
    context = {'form':form}
    return render(request, template_name, context)


def product_review(request, product_id):
    form = ReviewModelForm()
    if request.method == 'POST':
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.product = Product.objects.get(id = product_id)
            obj.save()
            return redirect('single_product', product_id)

    template_name = 'product_app/review.html'
    context = {'form':form}
    return render(request, template_name, context)

def show_review(request, pk):
    objs = ProductReview.objects.all(id=pk)
    return render(request, 'product_app/single_product.html', {'data':objs})

def customer_review(request, pk):
    obj = ProductReview.objects.get(id=pk)
    if request.user:
        obj = ProductReview.objects.filter(created_by=obj.created_by)
        return render(request, 'product_app/customer_review.html', {'data':obj})



def delete_review(request, pk):
    review = get_object_or_404(ProductReview, id=pk)

    if request.user == review.created_by:
        product_id = review.product.id
        review.delete()
        return redirect('single_product', pk=product_id)
    return redirect('home')  # Fallback