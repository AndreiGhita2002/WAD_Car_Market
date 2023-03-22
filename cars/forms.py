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
    PRICES = (0, 1000, 2000, 3000, 4000, 5000, 10_000, 20_000)

    title = forms.CharField(max_length=50, help_text='Posting Title', required=False)
    # todo: implement and test these:
    # condition = forms.ChoiceField(choices=Car.CONDITION, required=False)
    # brand = forms.ChoiceField(choices=Car.CAR_BRANDS, required=False)
    # # todo: add model choices instead of a string field
    # model = forms.CharField(max_length=18, help_text='Model', required=False)
    # num_of_seats = forms.ChoiceField(choices=Car.NUM_OF_SEATS, required=False)
    # fuel_type = forms.ChoiceField(choices=Car.FUEL, required=False)
    # year = forms.ChoiceField(choices=Car.YEARS, required=False)
    # colour = forms.ChoiceField(choices=Car.COLOURS, required=False)
    # min_price = forms.ChoiceField(choices=PRICES, required=False)
    # max_price = forms.ChoiceField(choices=PRICES, required=False)
    # location = forms.ChoiceField(choices=Car.LOCATIONS, required=False)

    def get_search_url(self):
        return 'title:' + self.cleaned_data['title']

