from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Slides, MainContent, SubContent
from .forms import SubContentForm


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
@login_required
def manage(request):
    return render(request, 'management/manage.html')


# Will show specific sub content details
def sub_detail(request, sub_id):
    subcontent = get_object_or_404(SubContent, pk=sub_id)
    context = {
        'subcontent': subcontent,
    }

    return render(request, 'home/sub_detail.html', context)


# Will add a sub content to the home
@login_required
def add_content(request):

    if request.method == 'POST':
        form = SubContentForm(request.POST, request.FILES)
        if form.is_valid():
            subcontent = form.save()
            messages.success(request, 'New content was successfully added!')
            return redirect(reverse('sub_detail', args=[subcontent.id]))
    else:
        form = SubContentForm()
    template = 'home/add_sub_content.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# Will edit sub content
@login_required
def edit_content(request, sub_id):

    subcontent = get_object_or_404(SubContent, pk=sub_id)
    if request.method == 'POST':
        form = SubContentForm(
            request.POST, request.FILES, instance=subcontent)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{subcontent.title} successfully updated Content!')
            return redirect(reverse('sub_detail', args=[subcontent.id]))
    else:
        form = SubContentForm(instance=subcontent)
        messages.success(request, f'You are editing {subcontent.title}')

    template = 'home/edit_sub_content.html'
    context = {
        'form': form,
        'subcontent': subcontent,
    }
    return render(request, template, context)


# Will delete sub content from home page
@login_required
def delete_content(request, sub_id):

    subcontent = get_object_or_404(SubContent, pk=sub_id)
    subcontent.delete()
    messages.success(request, f'{subcontent.title} was successfully deleted!')
    return redirect(reverse('home'))
