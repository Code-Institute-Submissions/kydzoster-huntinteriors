from django.shortcuts import render
from .models import Gallery


# Will show all products, sorting and search
def gallery(request):

    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery
    }
    return render(request, 'gallery/gallery.html', context)
