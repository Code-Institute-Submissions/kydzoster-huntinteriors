from django.shortcuts import render
from .models import Slides, MainContent, SubContent


def index(request):
    slides = Slides.objects.all()
    maincontent = MainContent.objects.all()
    subcontent = SubContent.objects.all()

    context = {
        'slides': slides,
        'maincontent': maincontent,
        'subcontent': subcontent,
    }
    return render(request, 'home/index.html', context)


def search(request):
    context = {}
    return render(request, 'home/search.html', context)


# Will show management
def manage(request):

    return render(request, 'management/manage.html')
