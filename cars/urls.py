from django.urls import path
from cars import views

app_name = 'cars'

# todo: implement dynamic urls for specific searches (used, new etc)

#  a lot of unused urls are commented right now
#  uncomment them when you implement them

urlpatterns = [
    path('details/', views.car_details, name='car_details'),
    path('sell/', views.sell_car, name='sell_your_car'),
    path('sell/add_car', views.add_car, name='add_car'),  # what's different between this and 'sell' ??
    # path('saved/', views.saved, name='saved'),

    # all of these go call views.browse through wrapper functions:
    path('', views.browse, name='cars_root'),
    path('used/', views.browse_used, name='cars_used'),
    path('new/', views.browse_new, name='cars_new'),
]
