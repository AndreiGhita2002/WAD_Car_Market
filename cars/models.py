from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator


def get_model_choices(car_models):
    out = []
    for brand in car_models:
        model = car_models.get(brand)
        for t in model:
            out.append(t)
    return tuple(out)


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
            ('taycan', 'Taycan'),
            ('panamera', 'Panamera'),
            ('macan', 'Macan'),
            ('cayman', 'Cayman'),
            ('boxter', 'Boxter'),
        ),

        'tesla': (
            ('model_3', 'Model 3'),
            ('model_x', 'Model X'),
            ('model_y', 'Model Y'),
            ('model_s', 'Model S'),
        ),

        'toyota': (
            ('yaris', 'Yaris'),
            ('corolla', 'Corolla'),
            ('chr', 'CH-R'),
            ('camry', 'Camry'),
            ('supra', 'Supra'),
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

    YEARS = (
        ('2023', '2023'),
        ('2022', '2022'),
        ('2021', '2021'),
        ('2020', '2020'),
        ('2019', '2019'),
        ('2018', '2018'),
        ('2017', '2017'),
        ('2016', '2016'),
        ('2015', '2015'),
        ('2014', '2014'),
        ('2013', '2013'),
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
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    )

    FUEL = (
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('electric', 'Electric'),
    )

    COLOURS = (
        ('white', 'White'),
        ('black', 'Black'),
        ('silver', 'Silver'),
        ('yellow', 'Yellow'),
        ('red', 'Red'),
    )

    LOCATIONS = (
        ('london', 'London'),
        ('birmingham', 'Birmingham'),
        ('manchester', 'Manchester'),
        ('leeds', 'Leeds'),
        ('liverpool', 'Liverpool'),
        ('glasgow', 'Glasgow'),
        ('edinburgh', 'Edinburgh'),
        ('aberdeen', 'Aberdeen'),
    )

    MODEL_CHOICES = get_model_choices(CAR_MODELS)

    # todo: add more validators

    # backend values:
    unique_car_id = models.AutoField(primary_key=True)

    # sorting values:
    # TODO: add cookies and stuff to count how many views a car listing gets
    #  maybe make it more advanced than just counting views
    views = models.IntegerField(default=0)

    # trading values:
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, verbose_name="Title", default="Unnamed Car", null=True)
    image = models.ImageField(upload_to='car_images/', verbose_name="Photo", null=True)
    price = models.PositiveIntegerField(verbose_name="Price", null=True, validators=[MaxValueValidator(100000000)])
    description = models.TextField(verbose_name="Description", null=True)
    date_posted = models.DateTimeField(auto_now_add=True, )
    location = models.CharField(max_length=10, choices=LOCATIONS, verbose_name="Location", null=True)

    # physical car values:
    brand = models.CharField(max_length=14, choices=CAR_BRANDS, verbose_name="Brand", null=True)
    model = models.CharField(max_length=18, choices=MODEL_CHOICES, verbose_name="Model", null=True)
    condition = models.CharField(max_length=4, choices=CONDITION, verbose_name="Condition", null=True)
    num_of_seats = models.PositiveIntegerField(choices=NUM_OF_SEATS, verbose_name="Number of seats", null=True)
    body_type = models.CharField(max_length=11, choices=BODY_TYPES, verbose_name="Body type", null=True)
    mileage = models.PositiveIntegerField(verbose_name="Mileage", null=True, validators=[MaxValueValidator(500000)])
    transmission = models.CharField(max_length=9, choices=GEARBOX, verbose_name="Transmission", null=True)

    fuel_type = models.CharField(max_length=8, choices=FUEL, verbose_name="Fuel type", null=True)
    year = models.CharField(max_length=4, choices=YEARS, verbose_name="Year", null=True)
    colour = models.CharField(max_length=6, choices=COLOURS, verbose_name="Colour", null=True)

    def __str__(self):
        return "Car:{" + self.title + "," + self.unique_car_id.__str__() + "}"
