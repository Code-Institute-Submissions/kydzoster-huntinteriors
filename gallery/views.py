from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Img
from .forms import ImgForm


# Will show all images, and search queries
def all_gallery(request):

    gallery = Img.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category']
            gallery = gallery.filter(category__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            # if search box is blank
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('gallery'))
            # if seach box is not blank
            queries = Q(name__icontains=query)\
                | Q(description__icontains=query)\
                | Q(category__icontains=query)
            gallery = gallery.filter(queries)

    context = {
        'gallery': gallery,
        'search_term': query,
        'categories': categories,
    }
    return render(request, 'gallery/gallery.html', context)


# Will show single image details
def image_detail(request, img_id):

    img = get_object_or_404(Img, pk=img_id)
    context = {
        'img': img,
    }
    return render(request, 'gallery/image_detail.html', context)


# will add image to gallery
@login_required
def add_image(request):

    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            messages.success(request, 'Image was successfully added!')
            return redirect(reverse('image_detail', args=[img.id]))
    else:
        form = ImgForm()
    template = 'gallery/add_image.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# Will edit image in the gallery
@login_required
def edit_image(request, img_id):

    img = get_object_or_404(Img, pk=img_id)
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES, instance=img)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated image!')
            return redirect(reverse('image_detail', args=[img.id]))
    else:
        form = ImgForm(instance=img)
        messages.info(request, f'You are editing {img.name}')
    template = 'gallery/edit_image.html'
    context = {
        'form': form,
        'img': img,
    }
    return render(request, template, context)


# Will delete an image from the gallery
@login_required
def delete_image(request, img_id):

    img = get_object_or_404(Img, pk=img_id)
    img.delete()
    messages.info(request, f'{img.name} was successfully deleted!')
    return redirect(reverse('gallery'))
