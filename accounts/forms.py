from django import forms
from .models import Artist, User, Category, Product, ProductImage



class UserModelForm(forms.ModelForm):
    same_as_shipping = forms.BooleanField(required=False, label="Billing address same as shipping address",
                                          initial=False)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'password', 'contact_number', 'alternate_contact_number', 'shipping_lane1', 'shipping_lane2', 'shipping_city', 'shipping_zip', 'shipping_state', 'shipping_country',
            'billing_lane1', 'billing_lane2', 'billing_city', 'billing_zip', 'billing_state', 'billing_country'
        ]

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


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        labels = {
            'category_name' : 'CATEGORY NAME',
            'description' : 'DESCRIPTION',
            'created_at' : 'CREATED_AT'
        }


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        labels = {
            'artist' : 'ARTIST',
            'pname' : 'PRODUCT NAME',
            'description' : 'DESCRIPTION',
            'price' : 'PRICE',
            'material' : 'MATERIAL',
            'weight' : ' WEIGHT',
            'dimensions' : 'DIMENSIONS',
            'COLOR_CHOICES' : 'COLOR_CHOICES',
            'color' : 'COLOR',
            'STYLE_CHOICES' : 'STYLE_CHOICES',
            'style' : 'STYLE',
            'category' : 'CATEGORY',
            'images' : 'IMAGES',
            'is_bestseller' : 'IS BESTSELLER',
            'created_at' : 'CREATED AT'
        }


class ProductImageModelForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'

        labels = {
            'product' : 'PRODUCT',
            'image_url' : 'IMAGE URL'
        }