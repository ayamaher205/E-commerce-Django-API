from django.db import models
from products.models import Product
from user.models import User

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    value = models.IntegerField(choices=[(1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5')], default=0)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.first_name} {self.product.name}"
