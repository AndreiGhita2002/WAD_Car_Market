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
    CONDITIONS = tuple([('', 'Conditions:')] + list(Car.CONDITION))
    BRANDS = tuple([('', 'Brands:')] + list(Car.CAR_BRANDS))
    MODELS = tuple([('', 'Models:')] + list(Car.MODEL_CHOICES))
    SEATS = tuple([('', 'Number of Seats:')] + list(Car.NUM_OF_SEATS))
    FUEL = tuple([('', 'Fuel Type:')] + list(Car.FUEL))
    YEARS = tuple([('', 'Year:')] + list(Car.YEARS))
    COLOURS = tuple([('', 'Colours:')] + list(Car.COLOURS))
    PRICES = [(1000, '1000'), (2000, '2000'), (3000, '3000'), (4000, '4000'), (5000, '5000'),
              (10000, '10000'), (20000, '200000')]
    MIN_PRICES = tuple([(0, 'Minimum Price:')] + PRICES)
    MAX_PRICES = tuple([(0, 'Maximum Price:')] + PRICES)

    title = forms.CharField(max_length=50, help_text='Posting Title', required=False)
    condition = forms.ChoiceField(choices=CONDITIONS, required=False, initial='')
    # todo: make these linked somehow:
    #  models should be linked with the brand choice
    brand = forms.ChoiceField(choices=BRANDS, required=False, initial='')
    model = forms.ChoiceField(choices=MODELS, required=False, initial='')
    # model = forms.CharField(max_length=18, help_text='Model', required=False)

    num_of_seats = forms.ChoiceField(choices=SEATS, required=False, initial='')
    fuel_type = forms.ChoiceField(choices=FUEL, required=False, initial='')
    year = forms.ChoiceField(choices=YEARS, required=False, initial='')
    colour = forms.ChoiceField(choices=COLOURS, required=False, initial='')
    min_price = forms.ChoiceField(choices=MIN_PRICES, required=False, initial=-1)
    max_price = forms.ChoiceField(choices=MAX_PRICES, required=False, initial=-1)
    # todo: implement this in a nice way
    # location = forms.ChoiceField(choices=Car.LOCATIONS, required=False)

    def get_search_url(self):
        print('Forms:')
        filters = []
        for field in self.fields:
            print(f' field:{field}')
            data = self.cleaned_data.get(field)
            print(f' -data:{data}')
            if data is not None and data != '':
                filters.append(str(field) + ':' + self.cleaned_data[str(field)])
                print(' -returned')
        return '-'.join(filters)

