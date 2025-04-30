from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserModelForm, ArtistModelForm
from .models import User, Artist


def user_create_view(request):
    form = UserModelForm()
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'accounts/user_form.html'
    context = {'form' : form}
    return render(request, template_name, context)

def user_retrieve_view(request):
    obj = User.objects.all()
    template_name = 'accounts/show_user.html'
    context = {'data':obj}
    return render(request, template_name, context)



def artist_create_view(request):
    form = ArtistModelForm()
    if request.method == 'POST':
        form = ArtistModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'accounts/artist_form.html'
    context = { 'form' : form}
    return render(request, template_name, context)

def artist_retrieve_view(request):
    obj = Artist.objects.all()
    template_name = 'accounts/show_artist.html'
    context = {'data':obj}
    return render(request, template_name, context)