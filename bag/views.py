from django.shortcuts import render, redirect


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
