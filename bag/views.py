from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from decimal import Decimal
from furnitures.models import Product
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe


# Renders the bag contents page
def view_bag(request):
    return render(request, 'bag/bag.html')


# Add a quantity of the specified product to the shopping bag
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


@csrf_exempt
def create_checkout_session(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
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

    grand_total = delivery + total

    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            print(grand_total)
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'bag/success?session_id=\
                    {CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'bag/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {'price_data': {
                        'currency': 'usd', 'product_data': {'name': 'Hunt-interiors cart', }, 'unit_amount': round(grand_total*100), }, 'quantity': 1, }],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def success(request):
    message = "Thanks for choosing us"

    return render(request, 'bag/success.html', {'message': message})
