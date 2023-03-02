from django import forms
from .models import Car


class CarListingForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = fields = ['price', 'brand', 'model', 'condition', 'description', 'date_posted', 'image',
                           'num_of_seats', 'body_type', 'mileage', 'gearbox', 'fuel_type', 'year_of_manufacture',
                           'colour', 'location']

        exclude = ['unique_car_id', 'seller']
