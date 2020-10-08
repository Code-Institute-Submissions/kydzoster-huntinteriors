from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Services
from .forms import ServicesForm


def services(request):
    services = Services.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'services/services.html', context)


# Will show specific service details
@login_required
def services_detail(request, serv_id):
    services = get_object_or_404(Services, pk=serv_id)
    context = {
        'services': services,
    }
    return render(request, 'services/services_detail.html', context)


# Will add a service to the services
@login_required
def add_services(request):

    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            services = form.save()
            messages.success(request, 'New Service was successfully added!')
            return redirect(reverse('services_detail', args=[services.id]))
    else:
        form = ServicesForm()
    template = 'services/add_services.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# Will edit services
@login_required
def edit_services(request, serv_id):

    services = get_object_or_404(Services, pk=serv_id)
    if request.method == 'POST':
        form = ServicesForm(
            request.POST, request.FILES, instance=services)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{services.title} was successfully updated!')
            return redirect(reverse('services_detail', args=[services.id]))
    else:
        form = ServicesForm(instance=services)
        messages.success(request, f'You are editing {services.title}')

    template = 'services/edit_services.html'
    context = {
        'form': form,
        'services': services,
    }
    return render(request, template, context)


# Will delete services from services page
@login_required
def delete_services(request, serv_id):

    services = get_object_or_404(Services, pk=serv_id)
    services.delete()
    messages.success(request, f'{services.title} was successfully deleted!')
    return redirect(reverse('home'))
