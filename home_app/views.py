from django.shortcuts import render, redirect
from product_app.models import Product
from django.db.models import Q

# Create your views here.
'''
def home_view(request):
    template_name='home_app/home.html'
    context = {}
    return render(request, template_name, context)
'''

def product_show_view(request):
    context = {}
    if request.method == 'GET' and request.GET:
        search = request.GET.get('searches') or request.GET.get('search') or request.GET.get('srch')
        if search:
            if 'searches' in request.GET:
                objs = Product.objects.filter(Q(category__category_name__contains = search) | Q(artist__user__first_name__contains = search))
                context['data']= objs
            elif 'search' in request.GET:
                objs = Product.objects.filter(Q(category__category_name = search))
                context['data']= objs
            elif 'srch' in request.GET:
                objs = Product.objects.filter(Q(price__contains = search) or Q(medium__contains = search) or Q(style__contains = search))
                context['data']= objs
    else:
        context['data']= Product.objects.all()
    template_name = 'home_app/home.html'
    return render(request, template_name, context)






def faqs_view(request):
    context = {}
    template_name = 'home_app/faqs.html'
    return render(request, template_name, context)
