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

def product_show_view(request):
    obj = Product.objects.all()
    template_name = 'product_app/show_product.html'
    context = {'data':obj}
    return render(request, template_name, context)