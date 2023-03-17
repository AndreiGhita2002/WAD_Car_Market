# Generated by Django 4.1.7 on 2023-03-17 15:29

import cars.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='gearbox',
        ),
        migrations.RemoveField(
            model_name='car',
            name='year_of_manufacture',
        ),
        migrations.AddField(
            model_name='car',
            name='title',
            field=models.CharField(default='exit', max_length=40, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='exit', max_length=9, verbose_name='Transmission'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.CharField(default='exit', max_length=4, validators=[cars.validators.is_valid_year], verbose_name='Year'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('saloon', 'Saloon'), ('estate', 'Estate'), ('coupe', 'Coupe'), ('hatchback', 'Hatchback'), ('suv', 'SUV'), ('convertible', 'Convertible')], max_length=11, verbose_name='Body type'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('audi', 'Audi'), ('bmw', 'BMW'), ('ford', 'Ford'), ('jaguar', 'Jaguar'), ('land_rover', 'Land Rover'), ('mercedes_benz', 'Mercedes-Benz'), ('nissan', 'Nissan'), ('porsche', 'Porsche'), ('tesla', 'Tesla'), ('toyota', 'Toyota')], max_length=14, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='car',
            name='colour',
            field=models.CharField(choices=[('white', 'White'), ('black', 'Black'), ('silver', 'Silver'), ('yellow', 'Yellow'), ('red', 'Red')], max_length=6, verbose_name='Colour'),
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('used', 'Used')], max_length=4, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('diesel', 'Diesel'), ('petrol', 'Petrol'), ('electric', 'Electric')], max_length=8, verbose_name='Fuel type'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, upload_to='car_images/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='location',
            field=models.CharField(choices=[('london', 'London'), ('birmingham', 'Birmingham'), ('manchester', 'Manchester'), ('leeds', 'Leeds'), ('liverpool', 'Liverpool'), ('glasgow', 'Glasgow'), ('edinburgh', 'Edinburgh'), ('aberdeen', 'Aberdeen')], max_length=10, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(verbose_name='Mileage'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(choices=[('a3', 'A3'), ('a4_avant', 'A4 Avant'), ('q7', 'Q7'), ('a6', 'A6'), ('a5', 'A5'), ('e_tron', 'E-tron'), ('1_series', '1 Series'), ('3_series', '3 Series'), ('4_series', '4 Series'), ('5_series', '5 Series'), ('x5', 'X5'), ('ix3', 'IX3'), ('focus', 'Focus'), ('puma', 'Puma'), ('monedo', 'Monedo'), ('mustang', 'Mustang'), ('xf', 'Xf'), ('a3', 'A3'), ('f_pace', 'F-pace'), ('e_pace', 'I-pace'), ('xe', 'XE'), ('f_type', 'F-type'), ('range_rover_evoque', 'Range Rover Evoque'), ('range_rover_velar', 'Range Rover Velar'), ('range_rover', 'Range Rover'), ('discovery', 'Discovery'), ('a_class', 'a Class'), ('c_class', 'c Class'), ('e_class', 'e Class'), ('g_class', 'G Class'), ('eqa', 'EQA'), ('eqs', 'EQS'), ('micra', 'Micra'), ('leaf', 'Leaf'), ('gtr', 'GT-R'), ('juke', 'Juke'), ('qashqai', 'Qashqai'), ('taycan', 'Taycan'), ('panamera', 'Panamera'), ('macan', 'Macan'), ('cayman', 'Cayman'), ('boxter', 'Boxter'), ('model_3', 'Model 3'), ('model_x', 'Model X'), ('model_y', 'Model Y'), ('model_s', 'Model S'), ('yaris', 'Yaris'), ('corolla', 'Corolla'), ('chr', 'CH-R'), ('camry', 'Camry'), ('supra', 'Supra'), ('a3', 'A3')], max_length=18, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='num_of_seats',
            field=models.PositiveIntegerField(choices=[(2, '2'), (4, '4'), (5, '5'), (7, '7'), (8, '8')], verbose_name='Number of seats'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[cars.validators.is_positive], verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='car',
            name='unique_car_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
