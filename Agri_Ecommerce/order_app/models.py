# order_app/models.py

from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('product_app.Product', on_delete=models.CASCADE, default=1)  # Set a default ID here
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} for {self.product.name}"
