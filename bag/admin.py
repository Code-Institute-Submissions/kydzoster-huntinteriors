from django.contrib import admin
from .models import PurchasedProduct, Invoice


admin.site.register([PurchasedProduct, Invoice])
