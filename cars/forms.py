from django import forms

from .models import Car


class CarListingForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['title', 'brand', 'model', 'price', 'condition', 'description', 'image',
                           'num_of_seats', 'body_type', 'mileage', 'transmission', 'fuel_type', 'year',
                           'colour', 'location']

        exclude = ['unique_car_id', 'views', 'seller', 'date_posted']


class CarSearchForm(forms.Form):
    title = forms.CharField(max_length=50, help_text='Posting Title', required=False)
    condition = forms.ChoiceField(choices=Car.CONDITION, required=False)
    brand = forms.ChoiceField(choices=Car.CAR_BRANDS, required=False)
    # todo: finish
