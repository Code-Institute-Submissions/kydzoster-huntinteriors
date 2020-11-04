from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


# will show all products
def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'furnitures/products.html', context)


# Will show a single product detail
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'furnitures/product_detail.html', context)


# will add a single product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f'{product.name} was successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductForm()
    template = 'furnitures/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# will show a single product details
@login_required
def edit_product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(
            request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{product.name} successfully updated!')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductForm(instance=product)
        messages.success(request, f'You are editing {product.name}')

    template = 'furnitures/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


# Will delete product from shop
@login_required
def delete_product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} was successfully deleted!')
    return redirect(reverse('products'))
