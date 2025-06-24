
from django.db import models
from accounts.models import CustomUser
from product_app.models import Product
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# # Create your models here.


class CartItem(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=0)
        price = models.CharField(max_length=30)
        date_added = models.DateTimeField(auto_now_add=True)

        
                