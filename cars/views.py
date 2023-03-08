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

    parameter args decides what to filter the car listings by

    for example:
        - /cars/used/ calls with args="condition:used"
        - if you are looking for new audi cars you call with args="condition:new,car_brand:audi"
        - if you are looking for the 3rd page of searches do args="page:2" (counting starts at 0)
        - all of these requirements can be combined with ','
    """
    filter_dict = get_filter_dict(args)
    filtered_cars, context_dir = filter_cars(Car.objects, filter_dict)

    start = CARS_PER_PAGE * int(filter_dict['page'])
    end = start + CARS_PER_PAGE
    sorted_cars = filtered_cars.order_by('-views')[start:end]  # default sort by views
    context_dir['carlist'] = sorted_cars

    return render(request, 'browse.html', context=context_dir)


def car_details(request):
    # todo: write this
    context_dir = {}
    # also todo: remember to increment view of the shown car (with cookies ideally)
    return render(request, 'car_details.html', context=context_dir)


# helper functions for browse():
def get_filter_dict(filters):
    if filters == "":
        return {}
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
    if filter_dict.get('page', None) is None:
        filter_dict['page'] = '0'
    return filter_dict


def filter_cars(car_objects, filter_dict):
    context_dir = {}
    filtered_cars = Car.objects
    # basic condition check; this will be expanded
    # todo: expand this
    if filter_dict.get('condition', -1) != -1:
        context_dir['car_condition'] = filter_dict['condition']
        filtered_cars = filtered_cars.filter(condition__exact=filter_dict['condition'])
    return filtered_cars, context_dir


# wrapper functions for browse():
def browse_used(request):
    return browse(request, args='condition:used')


def browse_new(request):
    return browse(request, args='condition:new')
