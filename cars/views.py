import sys

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from accounts.models import UserProfile
from cars.forms import CarListingForm, CarSearchForm
from cars.models import Car

# constant for how many car listings to show per page (maximum)
CARS_PER_PAGE = 20
# constant dict which tells filter_cars() how to search filter the car set
# depending on what the user searched for
SEARCH_TERMS = {
    'title': 'contains',
    'condition': 'exact',
    'brand': 'exact',
    'model': 'contains',
    'num_of_seats': 'exact',
    'fuel_type': 'exact',
    'year': 'exact',
    'colour': 'exact',
    'min_price': 'price',
    'max_price': 'price',
    'location': 'contains'
}


@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarListingForm(request.POST, request.FILES)
        if form.is_valid():
            car_listing = form.save(commit=False)
            car_listing.seller = request.user
            car_listing.save()
            return render(request, 'cars/success.html')
        else:
            return render(request, 'add_car.html', {'form': form})
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
        - if you are looking for new audi cars you call with args="condition:new-brand:audi"
        - if you are looking for the 3rd page of searches, do: args="page:2" (counting starts at 0)
        - all of these requirements can be combined with ',' or with '-'
    """
    if request.method == 'POST':
        form = CarSearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/cars/' + form.get_search_url())
    else:
        form = CarSearchForm()
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

        context_dir['page_title'] = create_title(filter_dict)
        context_dir['form'] = form

        print(f'List of Cars provided by browse(args=\'{args}\'):\n{sorted_cars}')
        return render(request, 'browse.html', context=context_dir)


def car_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    seller = car.seller
    print(seller)
    seller_first_name = seller.first_name
    print(seller_first_name)
    seller_last_name = seller.last_name
    print(seller_last_name)
    seller_email = seller.email

    context_dict = {
        'car': car,
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
        'related_cars': Car.objects.filter(brand=car.brand).exclude(pk=car.pk)[:4],
        'seller_first_name': seller_first_name,
        'seller_last_name': seller_last_name,
        'seller_email': seller_email,
    }

    car.views += 1
    car.save()
    return render(request, 'car_details.html', context=context_dict)


# helper functions for browse():
def get_filter_dict(filters):
    if filters == "":
        return {'page': 0}
    filter_dict, key, val, is_key = {}, "", "", True
    for c in filters:
        if c == ':':
            is_key = False
        elif c == ',' or c == '-':
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
    min_price = None
    max_price = None
    for category in SEARCH_TERMS.keys():
        if filter_dict.get(category, -1) != -1:
            if category == 'min_price':
                min_price = filter_dict.get('min_price')
            elif category == 'max_price':
                min_price = filter_dict.get('max_price')
            else:
                context_dir['car_' + category] = filter_dict[category]
                instruction = SEARCH_TERMS.get(category, -1)
                if instruction != -1:
                    lookup = "__".join([category, instruction])
                    filtered_cars = filtered_cars.filter(**{lookup: filter_dict[category]})
                else:
                    print('[Error] search failed!! check cars/views.filter_cars')
    if filter_dict.get('page', -1) != -1:
        context_dir['page'] = filter_dict['page']
    # todo: get min and max price filtering working
    if min_price is not None and type(min_price) == int:
        filtered_cars = filtered_cars.filter(price__gte=min_price)
    if max_price is not None and type(max_price) == int:
        filtered_cars = filtered_cars.filter(price__lte=max_price)
    return filtered_cars, context_dir


def create_title(filter_dict):
    title = 'Browsing '
    for key in filter_dict.keys():
        if key != 'page' and key != 'min_price' and key != 'max_price':
            title += filter_dict[key]
            title += ' '
    title += 'Cars'
    return title


# wrapper functions for browse():
def browse_used(request):
    return browse(request, args='condition:used')


def browse_new(request):
    return browse(request, args='condition:new')


def browse_all(request):
    return browse(request)
