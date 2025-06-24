# models.py
from django.db import models
from accounts.models import CustomUser
from product_app.models import Product  # Adjust this import as per your app structure
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Prevent duplicate wishlist entries

    def __str__(self):
        return f"{self.user.username} - {self.product.pname}"



