from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.models import User

# Create your views here.
def signin_view(request):
    if request.method == 'POST':
        uname = request.POST.get('nm')
        passw = request.POST.get('pw')

        user = authenticate(email = uname, password = passw)

        if user:
            login(request, user)
            return redirect('home')
        
    template_name = 'auth_app/signin.html'
    context = {}
    return render(request, template_name, context)