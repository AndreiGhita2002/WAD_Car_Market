import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'WAD_Car_Market.settings')

import django
django.setup()
from cars.models import Car
from accounts.models import UserProfile
from django.contrib.auth.models import User


def add_car(title, price=1000, description="", location="glasgow", brand="brand", model="default model", condition="new",
            num_of_seats=5, body_type="default body", mileage=500, transmission="gears", fuel_type="gas", year="2023",
            colour="blue", seller_id=0,image="static/images/default_car"): #remove image if anything breaks

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

    new_car.image = image #remove if anything breaks

    new_car.seller = UserProfile.objects.get(user_id=seller_id).user
    new_car.save()
    print(f" [new car] {new_car.title}: {new_car.description}")
    return new_car


def add_user(username, password='', first_name='First', last_name='Last', email='email@email.com', is_staff=False,
             profile_picture=None, address=''):
    # creating the user:
    new_user = User.objects.get_or_create(username=username)[0]
    new_user.password = password
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.email = email
    new_user.is_staff = is_staff
    new_user.save()
    # creating the profile
    new_profile = UserProfile.objects.get_or_create(user=new_user)[0]
    new_profile.profilePicture = profile_picture
    new_profile.address = address
    new_profile.save()
    print(f" [new user] {new_user.first_name} {new_user.last_name} {new_user.email}")


def populate_cars():
    print('Starting Car population script...')
    # tesla
    add_car("tesla 1", price=3000, description="A nice tesla car i had lying around.", location='liverpool',
            brand="tesla", model='model_3', condition="used", num_of_seats=4, body_type='convertible', mileage=700,
            transmission='automatic', fuel_type='electric', year='2022', colour='blue', seller_id=1)
    add_car("tesla 2", price=2600, description="A nice tesla car i had lying around.", location='glasgow',
            brand="tesla", model='model_x', condition="used", num_of_seats=5, body_type='suv', mileage=890,
            transmission='manual', fuel_type='electric', year='2022', colour='black', seller_id=3)
    add_car("tesla 3", price=5500, description="I got this as a gift, but I hate Tesla so now im selling it.",
            location='birmingham', brand="tesla", model='model_y', condition="new", num_of_seats=5, body_type='suv',
            mileage=0, transmission='automatic', fuel_type='electric', year='2022', colour='grey', seller_id=1)
    # audi:
    add_car("audi 1", price=3070, description="I love money.", location='london',
            brand="audi", model='a3', condition="used", num_of_seats=4, body_type='convertible', mileage=700,
            transmission='automatic', fuel_type='electric', year='2022', colour='blue', seller_id=1)
    add_car("audi 2", price=2000, description="A nice audi car i had lying around.", location='london',
            brand="audi", model='a3', condition="used", num_of_seats=5, body_type='suv', mileage=890,
            transmission='manual', fuel_type='electric', year='2022', colour='black', seller_id=3)
    add_car("audi 3", price=5570, description="I got this as a gift, but I hate Audi so now im selling it.",
            location='birmingham', brand="audi", model='a3', condition="new", num_of_seats=5, body_type='suv',
            mileage=0, transmission='automatic', fuel_type='electric', year='2022', colour='grey', seller_id=1)

    add_car("awful car", description="awful old car", price=400_000, condition="used", year="1995", seller_id=1)
    add_car("cheap car", description="third car", brand="third", condition="new", price=5, year="2020", seller_id=3)
    print('... finished Car population script.')


def populate_users():
    print('Starting User population script...')
    add_user('andrei', password='iZi7R98dpyS82bW', first_name='andrei', last_name='ghita', is_staff=True, email='andrei@gmail.com')
    add_user('big_seller', password='iZi7R98dpyS92bW', first_name='big', last_name='seller', email='sellerman@gmail.com')
    add_user('some_buyer', password='iZi7R98dpyS72bW', first_name='some', last_name='buyer', email='buyerguy@gmail.com')
    add_user('john', password='iZi7R98dpyS62bW', first_name='john', email='john@yahoo.com')
    add_user('other_staff', password='iZi7R98dpyS52bW', first_name='not', last_name='andrei', is_staff=True, email='staff@gmail.com')
    print('... which has not been implemented yet')  # remove when you implement this


def clear_all():
    UserProfile.objects.all().delete()
    # doesn't work cause of the car_wishlist
    # >> django.db.utils.OperationalError: no such table: cars_car_user_wishlist
    # Car.objects.all().delete()


if __name__ == '__main__':
    clear_all()
    populate_users()
    populate_cars()
