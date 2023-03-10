from django import forms
from .models import Car


class CarListingForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = fields = ['price', 'title', 'brand', 'model', 'condition', 'description', 'image',
                           'num_of_seats', 'body_type', 'mileage', 'transmission', 'fuel_type', 'year',
                           'colour', 'location']

        exclude = ['unique_car_id', 'seller', 'date_posted']
