from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


# Will show all images, and search queries
def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            # if search box is blank
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))
            # if seach box is not blank
            queries = Q(name__icontains=query)\
                | Q(description__icontains=query)\
                | Q(category__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)


# Will show single image details
def image_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/image_detail.html', context)


# will add image to gallery
@login_required
def add_image(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only site owner can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Image was successfully added!')
            return redirect(reverse('image_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()
    template = 'products/add_image.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# Will edit image in the gallery
@login_required
def edit_image(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only site owner can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('image_detail', args=[product.id]))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    template = 'products/edit_image.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


# Will delete an image from the gallery
@login_required
def delete_image(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only site owner can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.info(request, f'{product.name} was successfully deleted!')
    return redirect(reverse('products'))
