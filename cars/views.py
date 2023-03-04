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


def browse(request, html_doc):  # browse helper function, used by browse_new() and browse_used()
    # TODO rn it only shows the first n cars; figure out a way to show cars between n and m?
    #  (depending on url maybe)
    cars_to_show = Car.objects.order_by('-views')[:CARS_PER_PAGE]  # default sort by popularity
    context_dir = {"carlist": cars_to_show}
    return render(request, html_doc, context=context_dir)


def browse_new(request):
    browse(request, 'new.html')


def browse_used(request):
    browse(request, 'used.html')


def car_details(request):
    context_dir = {}
    return render(request, 'car_details.html', context=context_dir)


def show_saved(request):
    pass


def show_brands(request):
    pass


def show_electric(request):
    pass


def saved(request):
    pass
