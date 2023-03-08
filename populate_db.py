import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from cars.models import Car


def populate_cars():
    print('Starting Car population script...')
    print('... which has not been implemented yet')  # remove when you implement this


def populate_users():
    print('Starting User population script...')
    print('... which has not been implemented yet')  # remove when you implement this


if __name__ == '__main__':
    populate_users()
    populate_cars()
