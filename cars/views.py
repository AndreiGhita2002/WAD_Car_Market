from django.shortcuts import render, redirect, get_object_or_404

from cars.forms import CarListingForm
from cars.models import Car

# constant for how many car listings to show per page (maximum)
CARS_PER_PAGE = 10
# constant dict which tells filter_cars() how to search filter the car set
# depending on what the user searched for
SEARCH_TERMS = {
    'title': 'search',
    'condition': 'exact',
    'brand': 'exact',
    'model': 'search',
    'num_of_seats': 'exact',
    'fuel_type': 'exact',
    'year': 'exact',
    'colour': 'exact'
}  # todo: add price and other stuff


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


def browse(request, args=""):
    """
    General view function for any page that shows multiple car listings on the page,
    like /cars/browse/, /cars/browse/used/, /cars/browse/new/ etc.

    parameter args decides what to filter the car listings by

    for example:
        - /cars/browse/used/ calls with args="condition:used"
        - if you are looking for new audi cars you call with args="condition:new,car_brand:audi"
        - if you are looking for the 3rd page of searches, do: args="page:2" (counting starts at 0)
        - all of these requirements can be combined with ','
    """
    filter_dict = get_filter_dict(args)
    filtered_cars, context_dir = filter_cars(Car.objects, filter_dict)

    sorted_cars = filtered_cars.order_by('-views')  # default sort by views

    if sorted_cars is not None:
        start = CARS_PER_PAGE * int(filter_dict['page'])
        end = min(start + CARS_PER_PAGE, sorted_cars.count())
        sorted_cars = sorted_cars[start:end]  # selecting a CARS_PER_PAGE number of cars
        context_dir['carlist'] = sorted_cars

    if context_dir.get('page', -1) == -1:
        context_dir['page'] = 0

    return render(request, 'browse.html', context=context_dir)


def car_details(request, car_id):

    car = get_object_or_404(Car, pk=car_id)

    context_dict = {
        'page_title': f'{car.year} {car.colour} {car.brand} {car.model}',
        'seller': car.seller,
        'car_title': car.title,
        'price': car.price,
        'image_url': car.image.url if car.image else None,
        'description': car.description,
        'date_posted': car.date_posted,
        'location': car.location,
        'brand': car.brand,
        'model': car.model,
        'condition': car.condition,
        'num_of_seats': car.num_of_seats,
        'body_type': car.body_type,
        'mileage': car.mileage,
        'transmission': car.transmission,
        'fuel_type': car.fuel_type,
        'year': car.year,
        'colour': car.colour,
    }
    # also todo: remember to increment view of the shown car (with cookies ideally)
    return render(request, 'car_details.html', context=context_dict)


# helper functions for browse():
def get_filter_dict(filters):
    if filters == "":
        return {'page': 0}
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

    for category in SEARCH_TERMS.keys():
        if filter_dict.get(category, -1) != -1:
            context_dir['car_' + category] = filter_dict[category]
            instruction = SEARCH_TERMS.get(category, -1)
            if instruction != -1:
                lookup = "__".join([category, instruction])
                filtered_cars = filtered_cars.filter(**{lookup: filter_dict[category]})
            else:
                print('[Error] search failed!! check cars/views.filter_cars')
    if filter_dict.get('page', -1) != -1:
        context_dir['page'] = filter_dict['page']
    return filtered_cars, context_dir


# wrapper functions for browse():
def browse_used(request):
    return browse(request, args='condition:used')


def browse_new(request):
    return browse(request, args='condition:new')


def browse_all(request):
    return browse(request)
