from django.shortcuts import render
from product_app.models import Product
# Create your views here.
'''
def home_view(request):
    template_name='home_app/home.html'
    context = {}
    return render(request, template_name, context)
'''

def product_show_view(request):
    obj = Product.objects.all()
    template_name = 'home_app/home.html'
    context = {'data':obj}
    return render(request, template_name, context)