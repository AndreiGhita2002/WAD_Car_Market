from django.urls import path
from cars import views

app_name = 'cars'

# todo: implement dynamic urls for specific searches (used, new etc)

#  a lot of unused urls are commented right now
#  uncomment them when you implement them

urlpatterns = [
    path('details/', views.car_details, name='car_details'),
    path('sell/', views.sell_car, name='sell_your_car'),
    path('', views.browse_cars, name='cars'),
    path('browse/', views.browse_cars, name='browse_cars'),
    # path('sell_your_car/list_car', views.add_car, name='list_car'),
    # path('saved/', views.saved, name='saved'),

    # these two should be made more dynamic (have them all call the same view)
    # path('used/', views.used_car, name='used'),
    # path('new/', views.new_car, name='new'),
]
