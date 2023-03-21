import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'WAD_Car_Market.settings')

import django
django.setup()
from cars.models import Car


def add_car(title, price=1000, description="", location="glasgow", brand="brand", model="default model", condition="new",
            num_of_seats=5, body_type="default body", mileage=500, transmission="gears", fuel_type="gas", year="2023",
            colour="blue"):
    new_car = Car.objects.get_or_create(title=title)[0]
    new_car.price = price
    new_car.description = description
    new_car.location = location
    new_car.brand = brand
    new_car.model = model
    new_car.condition = condition
    new_car.num_of_seats = num_of_seats
    new_car.body_type = body_type
    new_car.mileage = mileage
    new_car.transmission = transmission
    new_car.fuel_type = fuel_type
    new_car.year = year
    new_car.colour = colour
    new_car.save()
    return new_car


def populate_cars():
    print('Starting Car population script...')
    add_car("car 1", description="a nice normal car", brand="tesla", condition="used")
    add_car("car 2", description="awful old car", price=400_000, condition="used", year="1995")
    add_car("car 3", description="third car", brand="third", condition="new", price=5, year="2020")
    print('... finished Car population script.')


def populate_users():
    print('Starting User population script...')
    print('... which has not been implemented yet')  # remove when you implement this


if __name__ == '__main__':
    populate_users()
    populate_cars()
