from django.db import models
from accounts.models import Artist
from category_app.models import Category


# Create your models here.

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

