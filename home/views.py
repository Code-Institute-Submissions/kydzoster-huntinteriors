from django.shortcuts import render
from .models import Home, MainContent, SubContent


def index(request):
    homeslide = Home.objects.all()
    maincontent = MainContent.objects.all()
    subcontent = SubContent.objects.all()

    context = {
        'homeslide': homeslide,
        'maincontent': maincontent,
        'subcontent': subcontent,
    }
    return render(request, 'home/index.html', context)


def search(request):
    context = {}
    return render(request, 'home/search.html', context)
