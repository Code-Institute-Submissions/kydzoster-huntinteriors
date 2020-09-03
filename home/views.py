from django.shortcuts import render
from .models import Home


def index(request):
    homeslide = Home.objects.all()
    context = {'homeslide': homeslide}
    return render(request, 'home/index.html', context)


def search(request):
    context = {}
    return render(request, 'home/search.html', context)
