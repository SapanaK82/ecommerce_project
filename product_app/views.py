from django.shortcuts import render, redirect
from .forms import ProductModelForm, ProductImageModelForm
from .models import Product, ProductImage

# Create your views here.
def product_create_view(request):
    form = ProductModelForm()
    if request.method=='POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'product_app/product_form.html'
    context = {'form':form}
    return render(request, template_name, context)


#all product retrieve view

def product_show_view(request):
    obj = Product.objects.all()
    template_name = 'home_app/home.html'
    context = {'data':obj}
    return render(request, template_name, context)

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
            form.save
    template_name = 'product_app/product_image.html'
    context = {'form':form}
    return render(request, template_name, context)