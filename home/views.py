from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Slides, MainContent, SubContent
from .forms import TitleForm, SubContentForm


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


# Will add a title to the home
def add_title(request):
    if request.method == 'POST':
        form = TitleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Title was successfully added to the Home!'
                )
            return redirect(reverse('add_title'))
    else:
        form = TitleForm()

    template = 'home/add_title.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Will add a sub content to the home
def add_sub_content(request):
    if request.method == 'POST':
        form = SubContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Sub content was successfully added to the Home!'
                )
            return redirect(reverse('add_sub_content'))
    else:
        form = SubContentForm()

    template = 'home/add_sub_content.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
