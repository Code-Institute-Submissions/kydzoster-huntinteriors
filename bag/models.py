from django.db import models
from django.contrib.auth.models import User
from furnitures.models import Product
from shortuuidfield import ShortUUIDField


class PurchasedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = ShortUUIDField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(PurchasedProduct)
    shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)
    checkout_session_id = models.CharField(max_length=40, null=True)

    @property
    def grand_total(self):
        return self.shipping_cost + sum(
            (p.product.price for p in self.products.all()))
