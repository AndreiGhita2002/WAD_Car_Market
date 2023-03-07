from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# field validators for models

def is_positive(num):
    if num < 0:
        raise ValidationError(_('%(value) is not positive.'), params={'value': num})


def is_valid_year(year):
    year_int = int(year)
    if year_int < 1970 or year_int > datetime.now().year:
        raise ValidationError(_('%(value) needs to be value year (between 1950 and 2050).'),
                              params={'value': year_int})
