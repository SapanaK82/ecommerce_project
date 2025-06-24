from django import forms
from .models import Artist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
import re

CustomUser = get_user_model()

#----------------------user form to register first time with password ---------------------------
class UserModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact_number = forms.CharField(max_length=15)
    is_artist = forms.BooleanField()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # hash the password
        if commit:
            user.save()
        return user
    
                        
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 
                  'contact_number', 'address', 'is_artist')
        widgets = {
            'password' : forms.PasswordInput(),
            'is_artist': forms.CheckboxInput(attrs={'required': False})
        }
        help_texts = {
            'password': 'Password must be at least 8 characters, include uppercase, lowercase, a number, and a special character.',

        }
        
    
    def clean_password(self):
        password = self.cleaned_data['password']
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
        if not re.match(pattern, password):
            raise forms.ValidationError(
                "Password must be at least 8 characters long, include uppercase, lowercase, a number, and a special character."
            )
        return password


    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        self.fields['is_artist'].required = False
    

#-----to update the form having limited fields---------------------
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email',
            'address', 'contact_number',
        )
    
#--------------------------To update username and password------------------------------

class UsernamePasswordUpdate(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # hash the password
        if commit:
            user.save()
        return user


    

#----------Artist Registration--------------------------
class ArtistModelForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

        labels = {
        'user' : 'USER',
        'bio' : 'BIO',
        'portfolio_image' : 'PORTFOLIO_IMAGE',
        'profile_picture' : 'PROFILE_PICTURE',
        'category' : 'CATEGORY',
        'Address' : 'ADDRESS',
        'rating'  : 'RATINGS',
        'created_at' : 'CREATED_AT'
    }




