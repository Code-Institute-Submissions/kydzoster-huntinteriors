from django.shortcuts import render, get_object_or_404
from .models import Product


# will show all products
def all_products(request):

    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'furnitures/products.html', context)


# will show a single product details
def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'furnitures/product_detail.html', context)
