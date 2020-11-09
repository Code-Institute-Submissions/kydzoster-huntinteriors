from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import SlidesForm, TitleForm, ContactForm
from .models import Slides, MainContent
from testaments.models import Testament
from furnitures.models import Product


def index(request):
    slides = Slides.objects.all()
    title = MainContent.objects.all()
    testament = Testament.objects.filter(approved=True).order_by('date')
    product = Product.objects.all().order_by('created_at')[:3]

    context = {
        'slides': slides,
        'title': title,
        'products': product,
        'testaments': testament
    }

    return render(request, 'home/index.html', context)


def search(request):
    context = {}
    return render(request, 'home/search.html', context)


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            subject = "You have a new Feedback from {} : {}".format(
                name, sender_email)
            message = form.cleaned_data["message"]
            sender = 'kydzoster@gmail.com'
            recipients = ['kydzoster@gmail.com']
            try:
                send_mail(
                    subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            form.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('contact.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form}


# Will show management
@login_required
def manage(request):
    return render(request, 'management/manage.html')


# Will show specific slides content details
@login_required
def slides_detail(request, slides_id):
    slides = Slides.objects.get(pk=slides_id)
    context = {
        'slides': slides,
    }
    return render(request, 'home/slides_detail.html', context)


# Will show title details
@login_required
def title_detail(request, title_id):
    title = get_object_or_404(MainContent, pk=title_id)
    context = {
        'title': title,
    }
    return render(request, 'home/title_detail.html', context)


# Will add a slides to the home
@login_required
def add_slides(request):

    if request.method == 'POST':
        form = SlidesForm(request.POST, request.FILES)
        if form.is_valid():
            slides = form.save()
            messages.success(request, 'New content was successfully added!')
            return redirect(reverse('slides_detail', args=[slides.id]))
    else:
        form = SlidesForm()
    template = 'home/add_slides.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# Will edit slides
@login_required
def edit_slides(request, slides_id):

    slides = get_object_or_404(Slides, pk=slides_id)
    if request.method == 'POST':
        form = SlidesForm(
            request.POST, request.FILES, instance=slides)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{slides.title} successfully updated!')
            return redirect(reverse('slides_detail', args=[slides.id]))
    else:
        form = SlidesForm(instance=slides)
        messages.success(request, f'You are editing {slides.title}')

    template = 'home/edit_slides.html'
    context = {
        'form': form,
        'slides': slides,
    }
    return render(request, template, context)


# Will edit slides
@login_required
def edit_title(request, title_id):

    title = get_object_or_404(MainContent, pk=title_id)
    if request.method == 'POST':
        form = TitleForm(
            request.POST, request.FILES, instance=title)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{title.title} successfully updated!')
            return redirect(reverse('title_detail', args=[title.id]))
    else:
        form = TitleForm(instance=title)
        messages.success(request, f'You are editing {title.title}')

    template = 'home/edit_title.html'
    context = {
        'form': form,
        'title': title,
    }
    return render(request, template, context)


# Will delete slides from home page
@login_required
def delete_slides(request, slides_id):

    slides = get_object_or_404(Slides, pk=slides_id)
    slides.delete()
    messages.success(request, f'{slides.title} was successfully deleted!')
    return redirect(reverse('home'))
