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
            ('a4', 'A4'),
            ('a5', 'A5'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),

        'bmw': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),

        'ford': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),

        'jaguar': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),

        'land_rover': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),

        'mercedes_benz': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
        ),

        'nissan': (
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
            ('a3', 'A3'),
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

    def __str__(self):
        return self.unique_car_id
