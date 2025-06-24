from importlib.metadata import requires

from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField(null=True)
    contact_number = models.BigIntegerField(unique=True, null=True, blank=True)
    is_artist = models.BooleanField(default=False)
    

class Artist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    portfolio_image = models.ImageField(upload_to='images/', blank=True)
    photo = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=30, choices=[('Painter', 'Painter'),
                                         ('Drawing','Drawing'),
                                         ('Sculptor','Sculptor'),
                                         ('Photgrapher','Photographer'),
                                         ('Print maker','Print maker')])
    Address = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} '



