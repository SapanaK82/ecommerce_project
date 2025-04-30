from django import forms
from .models import Artist, User

class UserModelForm(forms.ModelForm):
    same_as_shipping = forms.BooleanField(required=False, label="Billing address same as shipping address",
                                          initial=False)
    class Meta:
        model = User
        fields = '__all__' 

        labels = {
            'first_name' : 'FIRST NAME',
            'last_name' : 'LAST NAME',
            'email' : 'EMAIL',
            'password' : 'PASSWORD',
            'contact_number' : 'CONTACT NUMBER',
            'alternate_contact_number' : 'ALTERNATE CONTACT NUMBER',
        

    # shipping address
    'lane1' : 'LANE 1',
    'lane2' : 'LANE 2',
    'city' : 'CITY',
    'state' : 'STATE',
    'zipcode' : 'ZIPCODE',
    'country' : 'COUNTRY',
    # billing address
    'lane11' : 'LANE 1',
    'lane22' : 'LANE 2',
    'city1' : 'CITY',
    'state1' : 'STATE',
    'zipcode1' : 'ZIPCODE',
    'country1' : 'COUNTRY',
    'created_at' : 'CREATED_AT',
    'updated_at' : 'UPDATED_AT'
        }


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




