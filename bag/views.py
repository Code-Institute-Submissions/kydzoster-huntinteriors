from django.shortcuts import render, redirect, reverse, HttpResponse


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
