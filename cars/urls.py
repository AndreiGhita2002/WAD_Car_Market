from django.urls import path
from cars import views

app_name = 'cars'

urlpatterns = [
    path('used/', views.used_car, name='used'),
    path('new/', views.new_car, name='new'),
    path('car_details/', views.car_details, name='car_details'),
    path('sell_my_car/', views.sell_car, name='sell_my_car'),
    path('sell_my_car/list_car', views.new_car_listing, name='list_car'),
]
