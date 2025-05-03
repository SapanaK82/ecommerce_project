
from django.db import models
from accounts.models import User
from product_app.models import Product

# Create your models here.


class CartItem(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField()
        price = models.CharField(max_length=30)
        date_added = models.DateTimeField(auto_now_add=True)

        
                