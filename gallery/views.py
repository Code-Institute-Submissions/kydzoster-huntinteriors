from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Gallery
from .forms import GalleryForm


# Will show all gallery, sorting and search
def gallery(request):

    gallery = Gallery.objects.all()
    query = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "Please, provide a valid search criteria!"
                    )
                return redirect(reverse('gallery'))

            queries = Q(name__icontains=query) |\
                Q(design__icontains=query) |\
                Q(description__icontains=query)
            gallery = gallery.filter(queries)

    context = {
        'gallery': gallery,
        'search_term': query,

    }
    return render(request, 'gallery/gallery.html', context)


# Will show individual image details
def gallery_detail(request, gallery_id):

    gallery_detail = get_object_or_404(Gallery, pk=gallery_id)

    context = {
        'gallery_detail': gallery_detail
    }
    return render(request, 'gallery/gallery_detail.html', context)


# Will add images to gallery
def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Image was successfully added to the Gallery!'
                )
            return redirect(reverse('add_gallery'))
    else:
        form = GalleryForm()

    template = 'gallery/add_gallery.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
