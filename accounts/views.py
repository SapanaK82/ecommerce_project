from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from .forms import UserModelForm, CustomUserUpdateForm, UsernamePasswordUpdate, ArtistModelForm
from .models import Artist


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserModelForm

from .models import CustomUser
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.decorators import login_required

CustomUser = get_user_model()

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            is_artist = user_form.cleaned_data.get('is_artist')
            user.set_password(user_form.cleaned_data.get('password'))  # Hash password
            user.save()

            # Authenticate and login the user
            user = authenticate(
                username=user.username,
                password=user_form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)

            # If the user is marked as artist, redirect to artist form
            if is_artist:
                return redirect('artist_url')  # URL pattern for artist form

            return redirect('home')  # Or dashboard/home for normal users
    else:
        user_form = UserModelForm()

    return render(request, 'accounts/user_form.html', {'form': user_form})




def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('nm')
        password = request.POST.get('pw')

        user = authenticate(username=username, password = password)

        if user:
            login(request, user)
            return redirect('home')
            
    template_name = 'accounts/signin.html'
    context = {}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('signin')


def user_retrieve_view(request):
    obj = CustomUser.objects.all()
    template_name = 'accounts/show_user.html'
    context = {'data':obj}
    return render(request, template_name, context)

#------------To update fields ---------------------------------

def user_update_view(request,pk):
    obj = CustomUser.objects.get(id = pk)
    if request.user == obj:
        form = CustomUserUpdateForm(instance=obj)
        if request.method == 'POST':
            form = CustomUserUpdateForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('show_user')
    else:
        return HttpResponse('request denied')
    return render(request, 'accounts/user_form.html', {'form':form})

#-------------------to update username and password------------------

# def username_password_view(request, pk):
#     obj = CustomUser.objects.get(id=pk)
   
#     form = UsernamePasswordUpdate(instance = obj)
#     if request.method == 'POST':
#         form = UsernamePasswordUpdate(request.POST, request.FILES, instance=obj)
#         if form.is_valid():
#             form.save()

#     return render(request, 'auth_app/artist_signup.html', {'form':form})




from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404



def user_delete_view(request, pk):
    obj = get_object_or_404(CustomUser, id=pk)

    if request.user != obj:
        return HttpResponse('Request denied')

    if request.method == 'POST':
        obj.delete()
        return redirect('signup')  # make sure this URL name exists

    return render(request, 'accounts/delete_user.html', {'data': obj})

#-----------------------User Dashboard------
@login_required
def user_dashboard(request, pk):
    obj = CustomUser.objects.get(id=pk)
    # if request.user == obj.user:
    #     obj = CustomUser.objects.get(id=pk)
    #     return render(request, 'accounts/artist_page.html', {'data':obj})  # Or show 403 error
        
    # elif request.user:
    return render(request, 'accounts/user_dashboard.html', {'data':obj})
        




#-------------------------------------------artist crud-----------------------------------

# def artist_create_view(request):
#     form = ArtistModelForm()
#     if request.method == 'POST':
#         form = ArtistModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     template_name = 'accounts/artist_form.html'
#     context = { 'form' : form}
#     return render(request, template_name, context)

from django.contrib.auth.decorators import login_required

@login_required
def artist_create_view(request):
    # if not request.user.is_artist:
    #     return redirect('home')  # Prevent access if not artist

    if request.method == 'POST':
        form = ArtistModelForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.user = request.user
            artist.save()

            request.user.is_artist = True
            request.user.save()

            return redirect('home')
    else:
        form = ArtistModelForm()

    return render(request, 'accounts/artist_form.html', {'form': form})


def artist_retrieve_view(request):
    objs = Artist.objects.all()
    template_name = 'accounts/show_artist.html'
    context = {'data':objs}
    return render(request, template_name, context)

def artist_page_view(request, pk):
    obj = Artist.objects.get(id=pk)
    template_name = 'accounts/artist_page.html'
    context = {'data':obj}
    return render(request, template_name, context)

def artist_update_view(request, pk):
    obj = Artist.objects.get(id=pk)
    if request.user.id == obj.id:
        form = ArtistModelForm(instance=obj)
        if request.method == 'POST':
            form = ArtistModelForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('show_artist')
    else:
        return HttpResponse('request denied')
            
    return render(request, 'accounts/artist_form.html', {'form':form})

def artist_delete_view(request, pk):
    obj = get_object_or_404(Artist, id=pk)

    if request.user.id != obj.id:
        return HttpResponse('Request denied')

    if request.method == 'POST':
        obj.delete()
        return redirect('home')  # make sure this URL name exists

    return render(request, 'accounts/artist_delete.html', {'data': obj})

