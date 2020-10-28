from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from furnitures.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # for a product from the session
    for item_id, quantity in bag.items():
        # get product then
        product = get_object_or_404(Product, pk=item_id)
        # add its quantity to the total price and finally
        total += quantity * product.price
        # increment product count to the quantity
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

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
