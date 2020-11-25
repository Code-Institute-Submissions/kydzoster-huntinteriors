from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from decimal import Decimal
from .models import Invoice, PurchasedProduct
from furnitures.models import Product
from urllib.parse import unquote
import stripe
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages


# Renders the bag contents page
def view_bag(request):
    return render(request, 'bag/bag.html')


@login_required
def add_to_bag(request, item_id):
    # gets quantity from the form
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # saves user bag history in session memory without
    # loosing them while the session is active
    bag = request.session.get('bag', {})

    # this will calculate the bag content and
    # will increase the quantity of a product
    # by its id if the same product is already in the bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


# Adjust the quantity of the specified product to the specified amount
def adjust_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


# Remove the item from the shopping bag
def remove_from_bag(request, item_id):
    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


# Stripe addition
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@login_required
@csrf_exempt
def create_checkout_session(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    invoice = Invoice.objects.create(user=request.user)
    address = dict()
    try:
        address.update({
            "address": request.user.profile.address,
            "city": request.user.profile.city,
            "postal_code": request.user.profile.post_code,
        })
        if not (address["address"] and address["city"] and
                address["postal_code"]):
            messages.add_message(
                request,
                messages.ERROR, 'Please update your address information.')
            return redirect('edit')
    except:
        messages.add_message(
            request, messages.ERROR, 'Please update your address information.')
        return redirect('edit')
    invoice.address = unquote(
        address['address']+','+address['city']+','+address['postal_code'])
    invoice.save()

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        purchased_product = PurchasedProduct.objects.create(
            product=product, quantity=quantity)

        invoice.products.add(purchased_product)

        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # free delivery if it is less than threshold
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # will notify user how much they need to spend to get a free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    invoice.shipping_cost = delivery
    invoice.save()

    grand_total = delivery + total

    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'bag/success/?session_id=\
                    {CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'bag/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {'price_data': {
                        'currency': 'usd', 'product_data': {
                            'name': 'Hunt-interiors cart', }, 'unit_amount':
                                round(grand_total*100), }, 'quantity': 1, }],
            )
            invoice.checkout_session_id = unquote(checkout_session['id'])
            invoice.save()
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    del request.session['bag']
    invoice = Invoice.objects.get(
        checkout_session_id=request.GET.get('session_id').replace(' ', ''))

    subject = 'Your invoice'
    html_message = render_to_string('email.html', {'invoice': invoice})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = invoice.user.email
    copy = "swg1@inbox.lv"

    msg = EmailMultiAlternatives(subject, subject, from_email, [to, copy])
    msg.attach_alternative(html_message, "text/html")
    msg.fail_silently = False
    msg.send()
    message = f'{"Thanks For Choosing Hunt-Interiors"}'

    return render(request, 'bag/success.html', {'message': message})
