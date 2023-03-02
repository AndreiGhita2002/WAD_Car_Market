from django.shortcuts import render, redirect

from cars.forms import CarListingForm


def list_car(request):
    if request.method == 'POST':
        form = CarListingForm(request.POST, request.FILES)
        if form.is_valid():
            car_listing = form.save(commit=False)
            car_listing.owner = request.user
            car_listing.save()
            return redirect('')  # temporarily redirect user to home page, to be amended later on
    else:
        form = CarListingForm()
        return render(request, 'templates/cars/list_car.html', {'form': form})


def sell_car(request):
    pass


def car_details(request):
    pass


def new_car(request):
    pass


def used_car(request):
    pass


def show_saved(request):
    pass


def show_brands(request):
    pass


def show_electric(request):
    pass
