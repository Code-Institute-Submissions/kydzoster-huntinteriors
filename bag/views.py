from django.shortcuts import render


# Renders the bag contents page
def view_bag(request):
    return render(request, 'bag/bag.html')
