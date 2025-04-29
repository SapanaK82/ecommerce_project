from importlib.metadata import requires

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    alternate_contact_number = models.CharField(max_length=20, blank=True)
    #shipping address
    shipping_lane1 = models.CharField(max_length=25)
    shipping_lane2 = models.CharField(max_length=25)
    shipping_city = models.CharField(max_length=100)
    shipping_zip = models.CharField(max_length=20)
    shipping_state = models.CharField(max_length=25)
    shipping_country = models.CharField(max_length=25)
    #billiing Address
    billing_lane1 = models.CharField(max_length=25, blank=True)
    billing_lane2 = models.CharField(max_length=25, blank=True, null=True)
    billing_city = models.CharField(max_length=100, blank=True, null=True)
    billing_zip = models.CharField(max_length=20, blank=True, null=True)
    billing_state = models.CharField(max_length=25, blank=True, null=True)
    billing_country = models.CharField(max_length=25, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}'


class Artist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250)
    portfolio_image = models.ImageField(upload_to='images/', blank=True)
    profile_picture = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=30,choices=[('painting', 'Painting'),
                                         ('drawing','drawing'),
                                         ('sculpture','sculpture'),
                                         ('photography','photography'),
                                         ('print','print')])
    Address = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



class Category(models.Model):
    category_name = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    pname = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    material = models.CharField(max_length=20)
    weight = models.FloatField()
    dimensions = models.CharField(max_length=30)
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('black', 'Black'),
        ('white', 'White'),
    ]
    color = models.CharField(max_length=22, choices=COLOR_CHOICES)
    STYLE_CHOICES = [
        ('Abstract','Abstract'),
        ('Abstract Expressionism','Abstract Expressionism'),
        ('Fine Art', 'Fine Art'),
        ('Expressionism', 'Expressionism'),
        ('Figurative', 'Figurative'),
        ('Modern', 'Modern')]
    style = models.CharField(max_length=22, choices=STYLE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='p_images/')
    is_bestseller = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pname}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='p_images/')