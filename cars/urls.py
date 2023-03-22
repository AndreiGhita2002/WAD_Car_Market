from django.urls import path

from cars import views

app_name = 'cars'

urlpatterns = [
    path('browse/details/<int:car_id>', views.car_details, name='car_details'),
    path('sell', views.add_car, name='add_car'),
    # path('saved/', views.saved, name='saved'),  # todo: implement saved cars

    # all of these go call views.browse through wrapper functions:
    path('', views.browse_all, name='cars_root'),
    path('<str:args>', views.browse, name='cars_search'),
    path('used', views.browse_used, name='cars_used'),
    path('new', views.browse_new, name='cars_new'),
]
