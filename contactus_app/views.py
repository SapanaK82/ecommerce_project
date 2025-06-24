from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import ContactMessage
# Create your views here.

def contactus_view(request):
     form = ContactMessageForm()
     if request.method == 'POST':
         form = ContactMessageForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('home')
     return render(request, template_name ='contactus_app/contact.html', context={'form':form})


