from django.db import models
from stores.models import Store

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name