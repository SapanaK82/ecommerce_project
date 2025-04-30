from django.shortcuts import render, redirect
from .forms import CategoryModelForm
from .models import Category

# Create your views here.
def category_create_view(request):
    form = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'category_app/category_form.html'
    context = {'form' : form}
    return render(request, template_name, context)

def category_retrieve_view(request):
    obj = Category.objects.all()
    template_name = 'category_app/show_user.html'
    context = {'data':obj}
    return render(request, template_name, context)