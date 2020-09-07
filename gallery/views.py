from django.shortcuts import render, get_object_or_404
from .models import Gallery


# Will show all gallery, sorting and search
def gallery(request):

    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery
    }
    return render(request, 'gallery/gallery.html', context)


# Will show individual image details
def gallery_detail(request, gallery_id):

    gallery_detail = get_object_or_404(Gallery, pk=gallery_id)

    context = {
        'gallery_detail': gallery_detail
    }
    return render(request, 'gallery/gallery_detail.html', context)
