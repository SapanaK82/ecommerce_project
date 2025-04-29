from django.shortcuts import render

# Create your views here.
from .forms import UserModelForm, ProductModelForm, ProductImageModelForm, ArtistModelForm, CategoryModelForm


def user_view(request):
    form = UserModelForm()

    template_name = 'accounts/user_form.html'
    context = {'form' : form}
    return render(request, template_name, context)

def artist_view(request):
    form = ArtistModelForm()
    template_name = 'accounts/artist_form.html'
    context = { 'form' : form}
    return render(request, template_name, context)
