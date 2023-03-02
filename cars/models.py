from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    CAR_BRANDS = (
        ('audi', 'Audi'),
        ('bmw', 'BMW'),
        ('ford', 'Ford'),
        ('jaguar', 'Jaguar'),
        ('land_rover', 'Land Rover'),
        ('mercedes_benz', 'Mercedes-Benz'),
        ('nissan', 'Nissan'),
        ('porsche', 'Porsche'),
        ('tesla', 'Tesla'),
        ('toyota', 'Toyota'),
    )

    CAR_MODELS = {
        'audi': (
            ('a3', 'A3'),
            ('a4_avant', 'A4 Avant'),
            ('q7', 'Q7'),
            ('a6', 'A6'),
            ('a5', 'A5'),
            ('e_tron', 'E-tron'),
        ),

        'bmw': (
            ('1_series', '1 Series'),
            ('3_series', '3 Series'),
            ('4_series', '4 Series'),
            ('5_series', '5 Series'),
            ('x5', 'X5'),
            ('ix3', 'IX3'),
        ),

        'ford': (
            ('focus', 'Focus'),
            ('puma', 'Puma'),
            ('monedo', 'Monedo'),
            ('mustang', 'Mustang'),
        ),

        'jaguar': (
            ('xf', 'Xf'),
            ('a3', 'A3'),
            ('f_pace', 'F-pace'),
            ('e_pace', 'I-pace'),
            ('xe', 'XE'),
            ('f_type', 'F-type'),
        ),

        'land_rover': (
            ('range_rover_evoque', 'Range Rover Evoque'),
            ('range_rover_velar', 'Range Rover Velar'),
            ('range_rover', 'Range Rover'),
            ('discovery', 'Discovery'),
        ),

        'mercedes_benz': (
            ('a_class', 'a Class'),
            ('c_class', 'c Class'),
            ('e_class', 'e Class'),
            ('g_class', 'G Class'),
            ('eqa', 'EQA'),
            ('eqs', 'EQS'),
        ),

        'nissan': (
            ('micra', 'Micra'),
            ('leaf', 'Leaf'),
            ('gtr', 'GT-R'),
            ('juke', 'Juke'),
            ('qashqai', 'Qashqai'),
        ),

        'porsche': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),

        'tesla': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),

        'toyota': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),
    }

    BODY_TYPES = (
        ('saloon', 'Saloon'),
        ('estate', 'Estate'),
        ('coupe', 'Coupe'),
        ('hatchback', 'Hatchback'),
        ('suv', 'SUV'),
        ('convertible', 'Convertible'),
    )

    NUM_OF_SEATS = (
        (2, '2'),
        (4, '4'),
        (5, '5'),
        (7, '7'),
        (8, '8'),
    )

    CONDITION = (
        ('new', 'New'),
        ('used', 'Used'),
    )

    GEARBOX = (
        ('manual', 'Manual')
        ('automatic', 'Automatic')
    )

    FUEL = (
        ('diesel', 'Diesel')
        ('petrol', 'Petrol')
        ('electric', 'Electric')
    )

    MANUFACTURED_IN = (
        ('2018', '2018')
        ('2019', '2019')
        ('2020', '2020')
        ('2021', '2021')
        ('2022', '2022')
        ('2023', '2023')
    )

    COLOURS = (
        ('white', 'White')
        ('black', 'Black')
        ('silver', 'Silver')
        ('yellow', 'Yellow')
        ('red', 'Red')
    )

    unique_car_id = models.CharField(max_length=20, primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    brand = models.CharField(choices=CAR_BRANDS)
    model = models.CharField(choices="")
    condition = models.CharField(choices=CONDITION)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='car_images/', blank=True)
    num_of_seats = models.PositiveIntegerField(choices=NUM_OF_SEATS)
    body_type = models.CharField(choices=BODY_TYPES)
    mileage = models.PositiveIntegerField()
    gearbox = models.CharField(choices=GEARBOX)
    fuel_type = models.CharField(choices=FUEL)
    year_of_manufacture = models.CharField(choices=MANUFACTURED_IN)
    colour = models.CharField(choices=COLOURS)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.unique_car_id
