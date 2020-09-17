from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Slides, MainContent, SubContent
from .forms import TitleForm, SubContentForm, SlidesForm


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


# Will add a slides to the home
def slides(request):
    if request.method == 'POST':
        form = SlidesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Slides was successfully added to the Home!'
                )
            return redirect(reverse('slides'))
    else:
        form = SlidesForm()

    template = 'home/slides.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Will show Title details
def title_detail(request, main_id):
    maincontent = get_object_or_404(MainContent, pk=main_id)
    context = {
        'maincontent': maincontent,
    }

    return render(request, 'home/title_detail.html', context)


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


# Will show specific sub content details
def sub_detail(request, sub_id):
    subcontent = get_object_or_404(SubContent, pk=sub_id)
    context = {
        'subcontent': subcontent,
    }

    return render(request, 'home/sub_detail.html', context)


# Will add a sub content to the home
@login_required
def add_sub_content(request):
    form = SubContentForm()
    template = 'home/add_sub_content.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
