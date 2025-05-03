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
        return f'{self.first_name} {self.last_name}'


class Artist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    portfolio_image = models.ImageField(upload_to='images/', blank=True)
    photo = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=30, choices=[('PAINTING', 'Painting'),
                                         ('DRAWING','drawing'),
                                         ('SCULPTURE','sculpture'),
                                         ('PHOTOGRAPHY','photography'),
                                         ('PRINT','print')])
    Address = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} '



