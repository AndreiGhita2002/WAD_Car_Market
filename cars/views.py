from django.shortcuts import render, redirect

from cars.forms import CarListingForm
from cars.models import Car

# constant for how many car listings to show per page (maximum)
CARS_PER_PAGE = 10


def add_car(request):
    if request.method == 'POST':
        form = CarListingForm(request.POST, request.FILES)
        if form.is_valid():
            car_listing = form.save(commit=False)
            car_listing.owner = request.user
            car_listing.save()
            return redirect('')  # temporarily redirect user to home page, to be amended later on
    else:
        form = CarListingForm()
        return render(request, 'add_car.html', {'form': form})


def sell_car(request):
    pass


def browse(request, args=""):
    """
    General view function for any page that shows multiple car listings on the page,
    like /cars/, /cars/used/, /cars/new/ etc.

    :parameter 'args' decides what to filter car listings by
    for example:
        - /cars/used/ calls with args="condition:used"
        - if you are looking for new audi cars you call with args="condition:new,car_brand:audi"
    """

    # basic condition check; this will be expanded
    filter_dict = get_filter_dict(args)

    # TODO rn it only shows the first n cars; figure out a way to show cars between n and m?
    #  (depending on url maybe)
    cars_to_show = Car.objects.order_by('-views')[:CARS_PER_PAGE]  # default sort by popularity
    context_dir = {"carlist": cars_to_show}

    return render(request, 'browse.html', context=context_dir)


def car_details(request):
    # todo: write this
    context_dir = {}
    return render(request, 'car_details.html', context=context_dir)


# helper function for browse():
def get_filter_dict(filters):
    filter_dict, key, val, is_key = {}, "", "", True
    for c in filters:
        if c == ':':
            is_key = False
        elif c == ',':
            filter_dict[key] = val
            key, val = "", ""
            is_key = True
        elif is_key:
            key += c
        else:
            val += c
    filter_dict[key] = val
    return filter_dict


# wrapper functions for browse():
def browse_used(request):
    return browse(request, args='condition:used')


def browse_new(request):
    return browse(request, args='condition:new')
